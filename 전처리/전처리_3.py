dir_food = {
    '갈비구이':'galbigui',
    '계란찜':'gyeranjjim',
    '김치찌개':'kimchijjigae',
    '미역줄기볶음':'miyeokjulgibokkeum',
    '백김치':'baekkimchi',
    '불고기':'bulgogi',
    '삼계탕':'samgyetang',
    '순두부찌개':'sundubujjigae',
    '애호박볶음':'aehobakbokkeum',
    '후라이드치킨':'friedchicken'
    }

from PIL import Image, ImageOps
import os, sys, glob, time


raw_path =r'C:\Users\admin\Desktop\testCut' 
class_path = os.getcwd()

food_list = [i.split('\\')[-1] for i in glob.glob(raw_path+'/*')]
dir_name = [eng for kor, eng in dir_food.items() if kor in food_list]
# print(sorted(food_list))
# print(dir_name)
start = time.time() # 시작시간 
for kor, eng in zip(food_list, dir_name):
    Step = time.time() # 시작시간 
#     print(kor, eng)
    target_resize_dir =".\\data\\"+eng+"\\"
    if not os.path.isdir(target_resize_dir):
        os.makedirs(target_resize_dir)
    files = glob.glob(raw_path+f'/{kor}/*')
    # print(files)
    cnt = 1
    # size = (224, 224)
    size = (500, 500)
    area = (122,122,378,378)
    for file in files:
#         print(file)
        im = Image.open(file)
        im = im.convert('RGB')
        print("i: ", cnt, im.format, im.size, im.mode, file.split("\\")[-1])
        cnt+=1
        im = ImageOps.fit(im, size, Image.ANTIALIAS, 0, (0.5, 0.5))
        im = im.crop(area) # 이미지 자르기
        im.save(target_resize_dir+"resize_"+file.split("\\")[-1].split(".")[0]+".jpg", quality=100)
        im.rotate(90).save(target_resize_dir+"rotate_"+file.split("\\")[-1].split(".")[0]+".jpg", quality=100)
    
    
    Step_time=(time.time() - Step)/60           
    print("파트별 시간: %.2f[min]"%float(Step_time))
    
    
all_time=(time.time() - start)/60           
print("총 시간: %.2f[min]"%float(all_time))