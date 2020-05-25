# 파일이름으로 레이블 따기 
import os
# 현재 경로 확인 
print(os.getcwd())

'''
# json 방식 -> 틀 
{
    '대분류' :떡 ,
        { 경단':{
            '파일갯수':'1000',
            '파일이름':[]
                }
        }
}
'''

f_path = 'C:\kfood' # 파일 경로 
dir_path = os.path.abspath(f_path) # 경로 

S_list = list() # 소타이틀
B_list = list() # 대타이틀
file_list =list() # 개별 데이터 

# 반복문을 이용해 파일들을 추출한다. 
for dirpath, dirnames, filenames in os.walk(dir_path):
    B_list.append(dirnames)  # 대타이틀
    file_list.append(filenames) # 개별 이미지 데이터 

    for dirname in dirnames:
        S_list.append(dirname) # 소타이틀
print('DONE_NameExtraction')

# 데이터 확인 
# print(177-150,len(B_list),B_list) 
# print(len(S_list), S_list)

# 반복문을 이용해서 빈리스트를 제거한다. 
d_test = list()
for i in B_list:
    # print(i, len(i))
    if len(i) == 0 :
        del i
    else:
        d_test.append(i)
print('DONE_EmptyListDel')

# 데이터 이름을 알기쉽게 변경하고 데이터가 잘 저장되었는지 확인한다. 
All_list= d_test
# print(All_list,len(All_list))
# print(All_list[0]) # 대타이틀 
# print(All_list[1:]) # 소타이틀 

# 사전화 - 프로토 타입1 
test_1 = dict()
for key, new_key in zip(All_list[0], All_list[1:]):
    test_1[key]=new_key
# print(test_1) # 데이터 사전화 -> 프로토작업

# 사전화 프로토 타입 -2
test_2 = dict()
for key, new_key in zip(All_list[0], All_list[1:]):
    test_2[key]=dict({'ImgTitle': new_key})
# print(test_2)

# 사전화 프로토 타입 - 3
tmp = dict()
for i in range(len(All_list)-1):
    tmp[All_list[0][i]] = All_list[i+1]
# print(tmp)
print(len(file_list),len(file_list[0])) # 데이터 길이 확인 

# 이미지 파일이름 추출 
files = list()
for i in file_list:
    # print(i, len(i))
    if len(i) == 0 :
        del i
    else:
        files.append(i)
print('DONE_FileNameExtraction')
print('Files_Len:',len(files),'File1_Len:',len(files[0])) # 데이터 길이 확인 

# print('구이:',All_list[1])  # 데이터 확인

# 상위 : ImgTitle
a = dict()
for key, new_key in zip(All_list[0], All_list[1:]):
    for i, j in zip(new_key, files):
        a[i] = {'ImgLen':len(j) ,'ImgName': j}
        # break
# print(a,len(a))

# 상위 
food_list = dict()
for idx in range(len(All_list)-1):
#     print(i)
    for i ,j in enumerate(files):
        food_list[All_list[0][idx]]={'ImgTitle': a}
print(food_list)


# 제이슨 배포 
import json
print(os.getcwd())
# print(json.dumps(food_list, ensure_ascii=False, indent="\t") )

try:
    with open('food_label.json', 'w', encoding="utf-8") as f:
        json.dump(food_list,f, ensure_ascii=False, indent="\t")
except Exception as err :
    print(err, 'err발생')