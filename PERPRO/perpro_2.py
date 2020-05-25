# 기본
import os, glob
from PIL import Image
import numpy as np

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


dir_path = '/home/team/바탕화면/sample_cut/*'
files= glob.glob(dir_path+'/*')
# print(files)


err=list()
err_1 =list()
for i in files[:]:
    try:
        img = Image.open(i)
        print(img.size)
        # if img.size():
        #     pass
        # else:
        #     print(i)
    except:
        err.append(i)
        # print(img.size())

print(len(err), err)

for i in err:
    os.remove(i)


# img = load_img('/home/team/바탕화면/sample_cut/friedchicken/kimchijjigae0409.jpg')
# print(type(img))
# # print(img.size)

