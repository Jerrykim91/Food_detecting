#  지피유
from tensorflow.python.client import device_lib
from keras import backend

# 텐서플로우가 인식하는 디바이스 중에 GPU가 있는지 확인
print(device_lib.list_local_devices())
