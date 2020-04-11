# 이름 레이블따기 
import os

def search_path(dir_name = 'help'):    
    txt_err = '''
    - 여기 참고!
    ex) 만약 input => C:\input\train.csv에 위치한다면,
    1.  ->  '/'    -> 가장 최상의 디렉토리로 이동
        => / : root('C:')
    2.  ->  './'   -> 파일이 현재 디렉토리를 의미    
        => ./ : now_dir -> 내위치(=train.csv) -> train.csv
    3.  -> '../'   -> 상위 디렉토리로 이동
        => ../ : now_dir의 상단 폴더  -> input
    - 두단계 상위 디렉토리로 이동하려면 =>  '../../' 이렇게 사용
    '''

    if dir_name == 'help':
        print(txt_err)

    else:
        for dirname, _, filenames in os.walk(dir_name):  
        #     print(dirname, _, filenames)
            for filename in filenames:
#                 print(filename)
                print(os.path.join(dirname, filename))
    
# search_path('kfood')



import os

dir_path = os.path.abspath('kfood') # 경로 
# test = 'C:\test\kfood'
print(dir_path)
tmp = list()
tmp_test =list()

for dirpath, dirnames, filenames in os.walk(dir_path):
    # print(dirpath[14:],'1차')
    # print(dirpath[14:])
    tmp_test.append(dirpath[14:])

    for dirname in dirnames:
        print("\t", dirname)
        pass
    tmp.append(dirname)


    # for filename in filenames:
    #     print("\t", filename[:-4])
    #     # print(os.path.join(dirname, filename))
    #     # for num in range(1000+2):
    #     #     if filename[:4] == '.csv':
    #     #         print('10g')
    #     #         print(filename[:-4])
    #     break           
        # tmp.append(filename[:-4])
    # print()
# print(tmp,len(tmp))

# print(tmp.count())
'''

# 방식
{
    '대분류' :떡 ,
        { '중분류':'경단',
          '파일이름':'00',
                '파일':{}
                }

}


'''
# {
#     {name[i]}:'',
#     {name[]}

# } # 하나를 만들면 더해가면서 

# {
#     "떡" : [
#     {
#         "imgId" : "0001",
#         "imgtitle" : "경단",
#         "imgname" : [,,,]    
#     },
#     {
#         "imgId" : "0002",
#         "studentName" : "김우진",
#         "studentAddress" : "하계동"
#     },
#     {
#         "imgId" : "0003",
#         "studentName" : "유성진",
#         "studentAddress" : "중계동"
#     }],

#  # 끊고 
#     "professor" : [
#     {
#         "professorId" : "0001",
#         "professorName" : "양아무개",
#         "professorAddress" : "공릉동"
#     },
#     {
#         "professorId" : "0002",
#         "professorName" : "김아무개",
#         "professorAddress" : "하계동"
#     },
#     {
#         "professorId" : "0003",
#         "professorName" : "유아무개",
#         "professorAddress" : "중계동"
#     }]
# }

# # 작은거 부터 만들어야 해 
# {:}