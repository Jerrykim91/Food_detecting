import sys, os
import cv2
import numpy as np
from matplotlib import pyplot as plt
# keras
from keras import backend as K
from keras.preprocessing import image
from keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from keras.applications.inception_v3 import InceptionV3 , preprocess_input, decode_predictions
from keras.utils import plot_model
from keras.models import load_model
# tensorflow
import tensorflow as tf
from tensorflow.python.framework import ops


# 모델에 의해 299, 299로 정의 
H, W = 299, 299 # Input shape, defined by the model (model.input_shape)
num_classes = 1000
model_path = 'INPUT/MODEL/PATH'


############ Define model here ############################################
def build_model():
    """
    # 케라스 모델의 인스턴스를 리턴 받는다 
    Function returning keras model instance.
    # 모델은  여기서 훈련하고 로드하고 keras.applications서 로드 된다. 
    Model can be
     - Trained here
     - Loaded with load_model
     - Loaded from keras.applications
    """
    return InceptionV3(include_top=True, weights='imagenet')


def laod_model(path):
    # 이건 굳이 왜하닞 모르겠다... 필요하니까 했겠지 ?
	return load_model(path) 
############################################################################

# 이미지 로드 -> 전처리하기
def load_image(path, preprocess=True):
    """Load and preprocess image."""
    # 타겟 사이즈에 맞게 로드 
    x = image.load_img(path, target_size=(H, W))
    # 전처리가 true 일 경우 아래와 같이 진행한다. 
    if preprocess:
        x = image.img_to_array(x)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
    return x


# 이미지 처리  
def deprocess_image(x):
    """다음과 같이 정규화 -> 링크 들어가보기 :
    https://github.com/fchollet/keras/blob/master/examples/conv_filter_visualization.py
    """
    x = x.copy()
    if np.ndim(x) > 3:
        x = np.squeeze(x)
    # 텐서 정규화 -> 0의 센터 , 표준이 0.1인지를 확인 
    x -= x.mean()
    x /= (x.std() + 1e-5)
    x *= 0.1

    # clip to [0, 1]
    x += 0.5
    x = np.clip(x, 0, 1)

    # RGB 배열로 변환한다: convert to RGB array
    x *= 255
    if K.image_dim_ordering() == 'th':
        x = x.transpose((1, 2, 0))
    x = np.clip(x, 0, 255).astype('uint8')
    return x

# 정규화 -> L2 규범에 의해 텐서를 정규화하는 유틸리티 기능
def normalize(x):
    # 먼소린지... 뭔가 연산해서 넘겨주네 
    return (x + 1e-10) / (K.sqrt(K.mean(K.square(x))) + 1e-10)


# 가이드 모델 빌드하기 
def build_guided_model(load_model = False, path= None):
    """
    # 수정된 모델을 반환하는 함수 
    Function returning modified model.
    # 유도된 역전파에 따라서 모든 렐루 활성화 그리디언트의 함수가 변경 
    Changes gradient function for all ReLu activations
    according to Guided Backpropagation.
    """
    # 이부분은 잘 모르겠다. 
    if "GuidedBackProp" not in ops._gradient_registry._registry:
        # ops는 뭔가요 ? -> from tensorflow.python.framework import ops
        @ops.RegisterGradient("GuidedBackProp")
        def _GuidedBackProp(op, grad):
            dtype = op.inputs[0].dtype
            return grad * tf.cast(grad > 0., dtype) * \
                   tf.cast(op.inputs[0] > 0., dtype)

    g = tf.get_default_graph()

    if load_model == False:
	    with g.gradient_override_map({'Relu': 'GuidedBackProp'}):
	        return build_model() # build_model 리턴 

    elif load_model == True:
        with g.gradient_override_map({'Relu': 'GuidedBackProp'}):
            return load_model(path) # load_model(결로)를 리턴 

    return new_model   


def guided_backprop(input_model, images, layer_name):
    # 시각화 방법 ... ??
    """Guided Backpropagation method for visualizing input saliency."""
    input_imgs = input_model.input
    layer_output = input_model.get_layer(layer_name).output
    grads = K.gradients(layer_output, input_imgs)[0]
    backprop_fn = K.function([input_imgs, K.learning_phase()], [grads])
    grads_val = backprop_fn([images, 0])[0]

    return grads_val


def grad_cam(input_model, image, cls, layer_name):
    """GradCAM method for visualizing input saliency."""
    y_c = input_model.output[0, cls]
    conv_output = input_model.get_layer(layer_name).output
    grads = K.gradients(y_c, conv_output)[0] #y_c is the loss while conv_output is the w.r.t variables
    # Normalize if necessary
    # grads = normalize(grads)

    #Use keras wrapper to create a function which input input_model.input and output conv_output & grads
    gradient_function = K.function([input_model.input], [conv_output, grads]) 

    output, grads_val = gradient_function([image])
    output, grads_val = output[0, :], grads_val[0, :, :, :]

    #pool the gradients
    weights = np.mean(grads_val, axis=(0, 1))
    cam = np.dot(output, weights) #larger weights will mean that the features are more important

    # Process CAM
    cam = cv2.resize(cam, (H, W), cv2.INTER_LINEAR)
    cam = np.maximum(cam, 0)
    cam = cam / cam.max()
    return cam

def grad_cam_batch(input_model, images, classes, layer_name):

    """
    # 입력 성을 시각화하기위한 GradCAM 방법.
    GradCAM method for visualizing input saliency.
    #  grad_cam과 동일하지만 한 번의 실행으로 여러 이미지를 처리
    Same as grad_cam but processes multiple images in one run.
    """
    # 손실 
    loss = tf.gather_nd(input_model.output, np.dstack([range(images.shape[0]), classes])[0])
    layer_output = input_model.get_layer(layer_name).output
    grads = K.gradients(loss, layer_output)[0]
    gradient_fn = K.function([input_model.input, K.learning_phase()], [layer_output, grads])

    conv_output, grads_val = gradient_fn([images, 0])    
    weights = np.mean(grads_val, axis=(1, 2))
    cams = np.einsum('ijkl,il->ijk', conv_output, weights)
    
    # Process CAMs
    new_cams = np.empty((images.shape[0], H, W))
    for i in range(new_cams.shape[0]):
        cam_i = cams[i] - cams[i].mean()
        cam_i = (cam_i + 1e-10) / (np.linalg.norm(cam_i, 2) + 1e-10)
        new_cams[i] = cv2.resize(cam_i, (H, W), cv2.INTER_LINEAR)
        new_cams[i] = np.maximum(new_cams[i], 0)
        new_cams[i] = new_cams[i] / new_cams[i].max()
    
    return new_cams


def compute_saliency(model, guided_model, img_path, layer_name='mixed10', cls=-1, visualize=True, save=True):
    """
    # 세가지 접근방식을 모두 사용해서 계산. 
    Compute saliency using all three approaches.
        # 그라디언트를 계산하기위한 레이어
        -layer_name: layer to compute gradients;
        # 지역화 할 클래스 번호 (가장 가능성이 높은 클래스의 경우 -1)
        -cls: class number to localize (-1 for most probable class).
    """
    preprocessed_input = load_image(img_path)

    predictions = model.predict(preprocessed_input)
    top_n = 5
    top = decode_predictions(predictions, top=top_n)[0]
    classes = np.argsort(predictions[0])[-top_n:][::-1]
    print('Model prediction:')
    
    for c, p in zip(classes, top):
        print('\t{:15s}\t({})\twith probability {:.3f}'.format(p[1], c, p[2]))
    if cls == -1:
        cls = np.argmax(predictions)
    class_name = decode_predictions(np.eye(1, num_classes, cls))[0][0][1]
    print("Explanation for '{}'".format(class_name))
    
    gradcam = grad_cam(model, preprocessed_input, cls, layer_name)
    gb = guided_backprop(guided_model, preprocessed_input, layer_name)
    guided_gradcam = gb * gradcam[..., np.newaxis]

    if save:
        jetcam = cv2.applyColorMap(np.uint8(255 * gradcam), cv2.COLORMAP_JET)
        jetcam = (np.float32(jetcam) + load_image(img_path, preprocess=False)) / 2
        cv2.imwrite('gradcam.jpg', np.uint8(jetcam))
        cv2.imwrite('guided_backprop.jpg', deprocess_image(gb[0]))
        cv2.imwrite('guided_gradcam.jpg', deprocess_image(guided_gradcam[0]))
    
    if visualize:
        plt.figure(figsize=(15, 10))
        plt.subplot(131)
        plt.title('GradCAM')
        plt.axis('off')
        plt.imshow(load_image(img_path, preprocess=False))
        plt.imshow(gradcam, cmap='jet', alpha=0.5)

        plt.subplot(132)
        plt.title('Guided Backprop')
        plt.axis('off')
        plt.imshow(np.flip(deprocess_image(gb[0]), -1))
        
        plt.subplot(133)
        plt.title('Guided GradCAM')
        plt.axis('off')
        plt.imshow(np.flip(deprocess_image(guided_gradcam[0]), -1))
        plt.show()
        
    return gradcam, gb, guided_gradcam

def writefile(guided_model):
    with open('layers.txt','w') as file:
        for layer in guided_model.layers:
            file.write(layer.name)
            file.write('\n')
        

if __name__ == '__main__':
    model = build_model()
    guided_model = build_guided_model(False,model_path)
    writefile(guided_model)
    gradcam, gb, guided_gradcam = compute_saliency(model, guided_model, layer_name='mixed10',
                                             img_path=sys.argv[1], cls=-1, visualize=True, save=False)