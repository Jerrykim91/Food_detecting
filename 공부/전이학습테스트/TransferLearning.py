
# 전이학습 
# Google Inception v3 사용 
# !pip install tensorflow-hub 설치 -> 1.7 버전 이상 설치 


# 조건 1. 이미지의 정답을 나타내는 이름으로 폴더를 각각 만들어 주어야 함
# 조건 2. 각 폴더에 데이터를 넣고 직접 찍은 사진이나 인터넷에서 
#           무작위로 다운받은 파일을 최소 50장 이상 저장하고
# 조건 3. 그 폴더의 루트 폴더를 임의의 이름으로 저장한다음 retrain.py를 실행할때 
#         `--image_dir` 파라미터로 루트폴더 이름을 전달하면 트레인 러닝을 실행 할 수 있음   


# 고해상도 칼라이미지의 기본특징들이 이미 학습된 Google Inception v3 >>> retrain.py 
# retrain.py : https://github.com/tensorflow/hub/raw/r0.1/examples/image_retraining/retrain.py
# 트레이닝 데이터로 학습을 마친후 임의의 이미지를 분류하고 정확도를 확인
# label_image.py : https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/label_image/label_image.py

