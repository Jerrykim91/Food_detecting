
from selenium import webdriver
import urllib, requests, time, os
from base64 import b64encode # byte배열을 base64로 변경함.
import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup

#접근할 페이지 번호
page_num = 1



# print(os.getcwd())
food_list = []  
path = os.getcwd()+r'\\크롤링\\chromedriver.exe'
# driver = webdriver.Chrome(path)
# url = 'https://www.10000recipe.com/' # 기본 홈 

search = quote('계란찜')
# d_path = f'/recipe/list.html?q={search}' # 세부경로
# # 접속
# driver.get(url+d_path)
# time.sleep(3)
# driver.close()

#웹페이지의 소스를 가져온다.
# url = "https://www.kr.playblackdesert.com/BeautyAlbum?searchType=0&searchText=&categoryCode=0&classType=0,4,8,12,16,20,21,24,25,26,28,31,27,19,23,11,29,17,5&Page=1"

url =  'https://www.10000recipe.com/recipe/list.html?q='+search
fp = urllib.request.urlopen(url)
source = fp.read().decode('utf-8')
fp.close()

#소스에서 img_area 클래스 하위의 소스를 가져온다.
soup = BeautifulSoup(source, 'html.parser')
soup = soup.findAll("a", class_ = "thumbnail_over")

for i in soup:

    num+=1
    #이미지 경로를 받아온다.
    imgURL = i.find("img")["src"]

    urllib.request.urlretrieve(imgURL, path + str(num) + ".jpg")
    print(imgURL)
    break

