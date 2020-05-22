# 패키지 호출
import tensorflow as tf
#  지피유
# from tensorflow.python.client import device_lib
import keras.backend.tensorflow_backend as K
# from keras import backend


# 기본 팩 
import os, glob
import numpy as np


# 텐서플로우가 인식하는 디바이스 중에 GPU가 있는지 확인
# print(device_lib.list_local_devices())

# 
from keras.models import Sequential
from keras.layers import Conv2D , Activation, MaxPooling2D
from keras.layers import Flatten, Dense, Dropout

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

# 이미지 로드 
# img = load_img('/home/team/바탕화면/sample_cut/friedchicken/friedchicken0960.jpg')
# print(img.size)
 
# 배치 사이즈 
batch_size = 10

# 지피유_ 모델 
with K.tf.device('gpu:0'):
    model = Sequential([
        Conv2D(16, 3, padding='same', activation='relu', input_shape=(150, 150 ,3)),
        MaxPooling2D(),
        Conv2D(32, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Conv2D(64, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Flatten(),
        Dense(512, activation='relu'),
        Dense(1)
    ])


model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=False),
              metrics=['accuracy'])

# 이미지 전처
train_datagen = ImageDataGenerator(rescale=1./255,rotation_range=40, 
                                  zoom_range=0.8,
                                   width_shift_range=0.5, 
                                  height_shift_range=0.5, 
                                  #batch_size=30,
                                  )

# 학습
train_generator = train_datagen.flow_from_directory(
        '/home/team/바탕화면/sample_cut',  # 타겟 디렉토리
         target_size=(150, 150),  # 모든 이미지의 크기가 150x150로 조정
        batch_size=30,
        #rescale=1./255,
        #rotation_range=40, 
      #zoom_range=0.8,
       #width_shift_range=0.5, 
      #height_shift_range=0.5, 
        class_mode='binary')  # binary_crossentropy 손실 함수를 사용하므로 binary 형태로 라벨을 불러와야 합니다.


# 모델 돌리기 
hist=model.fit_generator(
train_generator,
steps_per_epoch=1000//batch_size,
#validation_data=validation_generator,
epochs=50)