# 모델 시각화(Model Visualisation)

from keras.models import load_model
from keras.utils import plot_model
from keras.preprocessing.image import load_img , img_to_array , ImageDataGenerator 
from keras.applications.inception_v3 import preprocess_input
import matplotlib.pyplot as plt
import cv2
import numpy as np

########################################################################################################

# functions
def show_images(unprocess=True):
    #used to visualise images
    plt.clf()
    
    def reverse_preprocess_input(x0):
        # 아래에 unprocessd에서 호출
        x = x0 / 2.0
        x += 0.5
        x *= 255.
        return x
    #import pdb;pdb.set_trace()
    for x in generatorTest: #그래프
        fig, axes = plt.subplots(nrows=8, ncols=4)
        fig.set_size_inches(8, 8)
        page = 0
        page_size = 32
        start_i = page * page_size
        # enumerate 사용해서 인덱스랑 같이 출력 -> 그래프 출력
        for i, ax in enumerate(axes.flat):
            img = x[0][i+start_i]
            # 위애서 만든 함수 호출 
            if unprocess:
                im = ax.imshow(reverse_preprocess_input(img).astype('uint8') )
            else:
                im = ax.imshow((img/2.0)+.5) # matplotlib는 0과 1 사이의 범위만 플롯을 할 수 있다.

            ax.set_axis_off()
            ax.title.set_visible(False)
            ax.xaxis.set_ticks([])
            ax.yaxis.set_ticks([])
            for spine in ax.spines.values():
                spine.set_visible(False)

        plt.subplots_adjust(left=0, wspace=0, hspace=0)
        plt.show()
        break

########################################################################################################

# 모델평가
def model_evaluate(model):
    # 손실, 정확도
    (eval_loss, eval_accuracy) = model.evaluate_generator(generatorTest,steps=None,verbose=1)
    print('Evaluating the:'.format(model.metrics_names))

    print("[INFO] accuracy: {:.2f}%".format(eval_accuracy * 100))
    print("[INFO] Loss: {}".format(eval_loss))

########################################################################################################


# 이미지 예측
def _predict_img(model,image,class_dictionary):

    # getting the predictions(예측하기)
    y_pred_prob = model.predict(image)
    class_predicted_ix = np.argmax(y_pred_prob, axis=1)

    # convert from ix to class label -> 클래스 레이블로 변환 
    inv_map = {v: k for k, v in class_dictionary.items()}
    label = inv_map[class_predicted_ix[0]]
    return label,y_pred_prob[0][class_predicted_ix[0]]

########################################################################################################


# 예측 시각화
def visualise_predict(model,imagePath,topNum = 5):
    # load the class_indices saved in the earlier step
    class_dictionary = np.load('class_indices.npy').item()
    num_classes = len(class_dictionary)
    # add the path to your test image below
    orig = cv2.imread(imagePath)

    print("[INFO] loading and preprocessing image...")
    image = load_img(imagePath, target_size=(299, 299))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    #do all the preprocessing for the images
    # important! otherwise the predictions will be '0'
    image = preprocess_input(image)


    y_pred_prob = model.predict(image)
    cls = np.argmax(y_pred_prob, axis=1)
    top_n_preds_ix = np.argpartition(y_pred_prob, -topNum)[:,-topNum:]
    
    #convert from ix to class label
    inv_map = {v: k for k, v in class_dictionary.items()}
    label = reversed([inv_map[x] for x in top_n_preds_ix[0]])
    probability = reversed([y_pred_prob[0,x] for x in top_n_preds_ix[0]])

    # get the prediction label
    #print("Predicted Label: {}, Probability: {}".format(label, probability))
    for c, p in zip(label, probability):
        print('\t{:15s}\twith probability {:.5f}'.format(c, p))

    toplabel = inv_map[cls[0]]
    # display the predictions with the image
    cv2.putText(orig, "Predicted: {}".format(toplabel), (10, 30),
                cv2.FONT_HERSHEY_PLAIN, 1.5, (43, 99, 255), 2)

    cv2.imshow("Classification", orig)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

########################################################################################################

# 모델 불러오기 
path = r'' 
model = load_model(path)


#saving the model architecture
file_name = 'modelArchitecture.png' 
plot_model(model, to_file=file_name)

# 단일 이미지 시각화(Visualising single image)
ImgUrl = r'C:\downloads\train\cheesecake\42503.jpg'
visualise_predict(model, ImgUrl, 5) # 위 예측 시각화 부분 참조 



# 이미지 배치 시각화(Visualising batches of imges)
testUrl =  r'F:\datasetv3\Test'

datagenTest = ImageDataGenerator(preprocessing_function = preprocess_input) # preprocess_input is the preprocessing function used in -> 전처리함수
                                                                            # original inceptionV3 model

generatorTest = datagenTest.flow_from_directory(
    testUrl,
    target_size=(299,299),
    batch_size=32,
    class_mode='categorical',
    shuffle=True)

# 예측 시각화 참조 
class_dictionary = np.load('class_indices.npy').item() # 
class_dictionary # output data은 음식 이름이랑 넘버

########################################################################################################

plt.clf()
inv_map = {v: k for k, v in class_dictionary.items()}

for x in generatorTest:
    fig, axes = plt.subplots(nrows=8, ncols=4)
    fig.set_size_inches(21, 14)
    page = 0
    page_size = 32
    start_i = page * page_size
    
    for i, ax in enumerate(axes.flat):
        
        # get predicted label and store as label
        img = x[0][i+start_i]
        img_expanded = np.expand_dims(img, axis=0)
        label, _ = _predict_img(model,img_expanded,class_dictionary)   
        
        # get true y_label
        y_ix = x[1][i+start_i]
        class_predicted_ix = np.nonzero(y_ix)
        y_label = inv_map[int(class_predicted_ix[0])]
        correct = label == y_label

        # draw image
        im = ax.imshow((img/2.0)+.5) #matplotlib can only plot between range of 0 and 1
        ax.set_axis_off()
        ax.title.set_visible(False)
        ax.xaxis.set_ticks([])
        ax.yaxis.set_ticks([])   
        
        # add the predicted and actual class
        print('predicted:{0} , actual:{1}'.format(label,y_label),correct)

        if correct:
            ax.text(0,0, 'Predicted:'+ label, size=10, rotation=0,
                 bbox=dict(boxstyle="round",ec='green',fc='green'))

        if not correct:
            ax.text(1,1, 'Predicted:'+ label, size=10, rotation=0,
                 bbox=dict(boxstyle="round",ec='brown',fc='brown'))
            ax.text(0,0, 'Actual:'+ y_label, size=10, rotation=0,
                 bbox=dict(boxstyle="round",ec='red',fc='red'))
            
        for spine in ax.spines.values():
            spine.set_visible(False)

    plt.subplots_adjust(left=0, wspace=1, hspace=0)
    plt.show() # 이미지 출력 
    break

########################################################################################################
