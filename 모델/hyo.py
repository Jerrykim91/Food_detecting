# 전이 학습 

import tensorflow as tf
import keras
from tensorflow.python.client import device_lib
from keras import backend


# gpu를 인식하는지 확인합니다. 모두 True가 나오면 됩니다.
print(tf.test.is_built_with_cuda())
print(tf.test.is_gpu_available(cuda_only=False, min_cuda_compute_capability=None))
#print(tf.config.list_pysical_devices('GPU'))


# ResNet50 불러오기 


from keras.applications import ResNet50
from keras.layers import Dense, Input, Activation
from keras.models import Model
from keras.callbacks import EarlyStopping
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.normalization import BatchNormalization
#from PIL import Image

PATH="/home/team/바탕화면/hyo"
train_datagen = ImageDataGenerator(rescale=1./255,validation_split=0.33)


# train_generator
train_generator = train_datagen.flow_from_directory(
        PATH,
        shuffle=True,
        seed=13,
        target_size=(224,224),
        batch_size=64,
        class_mode = 'categorical',
        subset="training")

val_generator = train_datagen.flow_from_directory(
        PATH,
        shuffle=True,
        seed=13,
        target_size=(224,224),
        batch_size=64,
        class_mode = 'categorical',
        subset="validation")

 
input = Input(shape=(224, 224, 3))
model = ResNet50(input_tensor=input, include_top=False, weights=None, pooling='max')
model.trainalbe = False
model.summary()

# number of classes
K = 4
x = model.output
x = Dense(1024, name='fully', init='uniform')(x)
x = BatchNormalization()(x)
x = Activation('relu')(x)
x = Dense(512, init='uniform')(x)
x = BatchNormalization()(x)
x = Activation('relu')(x)
# Dense의 맨 앞부분 내가 필요한 category수만큼 적어주면 된다
x = Dense(K, activation='softmax', name='softmax')(x)
model = Model(model.input, x)
model.summary()

model.compile(loss='mse',optimizer='adam',metrics=['accuracy'])
history = model.fit_generator(train_generator,steps_per_epoch=100,
                          validation_data=val_generator,validation_steps=15, 
                          epochs=50)
