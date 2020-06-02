
# 패키지 

from PIL import Image, ImageOps
import os, sys, glob, time

raw_path ='C:\\data_final'
class_path = os.getcwd()

name = ['국','구이','무침','김치'] 
dir_list = [i.split('\\')[-1] for i in glob.glob(raw_path+'/*')]

start = time.time() # 시작시간 
for newna in dir_list:
    Step = time.time() # 시작시간 
    print(newna)
    # 경로 => 'C:\\data'
    target_resize_dir ="C:\\food_data\\"+newna+"\\"
    if not os.path.isdir(target_resize_dir):
        os.makedirs(target_resize_dir)
    files = glob.glob(raw_path+f'/{newna}/*')
    print(len(files))
    
    cnt = 1
    size = (224, 224)
    for file in files:
        # print(file)
        im = Image.open(file)
        im = im.convert('RGB')
        # print(" cnt : ", cnt, im.format, im.size, im.mode, file.split("\\")[-1])
        cnt+=1
        im = ImageOps.fit(im, size, Image.ANTIALIAS, 0, (0.5, 0.5))
        im.save(target_resize_dir+"resize_"+file.split("\\")[-1].split(".")[0]+".jpg", quality=100)
        # im.rotate(90).save(target_resize_dir+"rotate_"+file.split("\\")[-1].split(".")[0]+".jpg", quality=100)

    Step_time=(time.time() - Step)/60   
    dir_ch = glob.glob(target_resize_dir+'/*')        
    print(len(dir_ch))
    print("파트별 시간: %.2f[min]"%float(Step_time))



all_time=(time.time() - start)/60          
print("총 시간: %.2f[min]"%float(all_time))
