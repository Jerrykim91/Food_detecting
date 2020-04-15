경로 추출
import os 

나는 각 폴더에있는 csv의 파일의 추출-> 동일한 이름 

정규식 ‘이름.csv’ 일치하는것만 출력

파일 디렉토리 이중 for 문으로 
돌려
for dirname in dirnames:
   for filename in filenames:
       if re.match(‘파일이름.csv’)== ture:
출력 그파일 풀 패스 출력
dir_path=list()# 포문 밖에서 작성

dir_path.apped(풀패스-150)

아니면 pass


리스트에 담은 경로를 
import pandas as pd
i=1
for check in dir_path:
 Print(check)
i += 1
food_name + f‘{i}’= pd.read_csv(check)
 출력 되면 
추출 데이터 열어 보고 쫙 읽어들여서 
각 파일 별로 리스트에 담기
