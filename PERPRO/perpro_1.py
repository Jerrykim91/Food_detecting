
# 패키지 
import os, glob
from PIL import Image

# 경로
filee= glob.glob(r'C:\Food_detecting\data')
filee=sorted(filee)
# 디렉토리 명 
food_dict = {
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


area = (250,250,750,750) # 잘라 낼 범위
error=list() # 에러 
for name in food_dict.keys():
    food_img = sorted(glob.glob(r'C:\Food_detecting\data'+ name +'/*'))
    for i in range(len(food_img)):
        # print(2)
        try:
            img = Image.open(food_img[i])
            # img=img.resize((1000,1000))
            cut_img = img.crop(area)
            
            print(cut_img,cut_img.size)
            # cut_img.save('/home/team/바탕화면/sample_cut/'+food_dict[name]+'/'+food_dict[name]+'{0:0>4}'.format(i)+'.jpg')
        except:
            error.append(food_img[i])
        break






"""
['/home/team/바탕화면/sample_cut/bulgogi/bulgogi0540.jpg', '/home/team/바탕화면/sample_cut/bulgogi/bulgogi0389.jpg', '/home/team/바탕화면/sample_cut/bulgogi/bulgogi0529.jpg', '/home/team/바탕화면/sample_cut/bulgogi/bulgogi0559.jpg', '/home/team/바탕화면/sample_cut/bulgogi/bulgogi0467.jpg', '/home/team/바탕화면/sample_cut/bulgogi/bulgogi0524.jpg', '/home/team/바탕화면/sample_cut/bulgogi/bulgogi0568.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0105.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0960.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0190.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0266.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0063.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0021.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0150.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0174.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0254.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0051.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0216.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0107.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0193.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0274.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0110.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0962.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0188.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0023.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0155.jpg', '/home/team/바탕화면/sample_cut/friedchicken/friedchicken0172.jpg', '/home/team/바탕화면/sample_cut/kimchijjigae/kimchijjigae0979.jpg', '/home/team/바탕화면/sample_cut/kimchijjigae/kimchijjigae0257.jpg', '/home/team/바탕화면/sample_cut/kimchijjigae/kimchijjigae0409.jpg', '/home/team/바탕화면/sample_cut/kimchijjigae/kimchijjigae0439.jpg', '/home/team/바탕화면/sample_cut/kimchijjigae/kimchijjigae0323.jpg', '/home/team/바탕화면/sample_cut/kimchijjigae/kimchijjigae0458.jpg', '/home/team/바탕화면/sample_cut/kimchijjigae/kimchijjigae0351.jpg', '/home/team/바탕화면/sample_cut/kimchijjigae/kimchijjigae0102.jpg', '/home/team/바탕화면/sample_cut/kimchijjigae/kimchijjigae0441.jpg', '/home/team/바탕화면/sample_cut/baekkimchi/baekkimchi0098.jpg', '/home/team/바탕화면/sample_cut/baekkimchi/baekkimchi0077.jpg', '/home/team/바탕화면/sample_cut/baekkimchi/baekkimchi0004.jpg', '/home/team/바탕화면/sample_cut/baekkimchi/baekkimchi0892.jpg', '/home/team/바탕화면/sample_cut/baekkimchi/baekkimchi0282.jpg', '/home/team/바탕화면/sample_cut/baekkimchi/baekkimchi0227.jpg', '/home/team/바탕화면/sample_cut/baekkimchi/baekkimchi0078.jpg', '/home/team/바탕화면/sample_cut/baekkimchi/baekkimchi0201.jpg', '/home/team/바탕화면/sample_cut/baekkimchi/baekkimchi0185.jpg', '/home/team/바탕화면/sample_cut/samgyetang/samgyetang0368.jpg', '/home/team/바탕화면/sample_cut/samgyetang/samgyetang0313.jpg', '/home/team/바탕화면/sample_cut/samgyetang/samgyetang0337.jpg', '/home/team/바탕화면/sample_cut/samgyetang/samgyetang0378.jpg', '/home/team/바탕화면/sample_cut/samgyetang/samgyetang0971.jpg', '/home/team/바탕화면/sample_cut/gyeranjjim/gyeranjjim0242.jpg', '/home/team/바탕화면/sample_cut/gyeranjjim/gyeranjjim0081.jpg', '/home/team/바탕화면/sample_cut/gyeranjjim/gyeranjjim0088.jpg', '/home/team/바탕화면/sample_cut/gyeranjjim/gyeranjjim0239.jpg', '/home/team/바탕화면/sample_cut/gyeranjjim/gyeranjjim0039.jpg', '/home/team/바탕화면/sample_cut/gyeranjjim/gyeranjjim0157.jpg', '/home/team/바탕화면/sample_cut/gyeranjjim/gyeranjjim0210.jpg', '/home/team/바탕화면/sample_cut/sundubujjigae/sundubujjigae0292.jpg', '/home/team/바탕화면/sample_cut/sundubujjigae/sundubujjigae0287.jpg', '/home/team/바탕화면/sample_cut/sundubujjigae/sundubujjigae0260.jpg', '/home/team/바탕화면/sample_cut/sundubujjigae/sundubujjigae0404.jpg', '/home/team/바탕화면/sample_cut/sundubujjigae/sundubujjigae0405.jpg', '/home/team/바탕화면/sample_cut/sundubujjigae/sundubujjigae0347.jpg', '/home/team/바탕화면/sample_cut/sundubujjigae/sundubujjigae0278.jpg', '/home/team/바탕화면/sample_cut/miyeokjulgibokkeum/miyeokjulgibokkeum0115.jpg', '/home/team/바탕화면/sample_cut/miyeokjulgibokkeum/miyeokjulgibokkeum0117.jpg', '/home/team/바탕화면/sample_cut/galbigui/galbigui0231.jpg', '/home/team/바탕화면/sample_cut/galbigui/galbigui0197.jpg', '/home/team/바탕화면/sample_cut/galbigui/galbigui0179.jpg', '/home/team/바탕화면/sample_cut/galbigui/galbigui0131.jpg']

"""
