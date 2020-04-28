# 이미지 크롤링 테스트 

import os , csv, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
root = os.path.join(BASE_DIR, 'src')

print(os.getcwd())

# 함수라인 
def ClickAction(xpath):
    # 패스 입력 
    target = driver.find_element_by_xpath(xpath)
    log = '클릭 엑션 동작'
    print(log)
    return target.click()



# 드라이버 옵션 
options = webdriver.ChromeOptions()
# options.add_argument('headless') 
options.add_argument("window-size=1920x1080")
# user-agent 
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  

name = '한국음식' 
name_eng = 'food'
main_path ='https://www.flickr.com' 
action_path = f'/search/?media=photos&tags={name}' # 변동 될 수 있음

# https://www.flickr.com/search/?text=%ED%95%9C%EA%B5%AD%EC%9D%8C%EC%8B%9D

url = main_path + action_path
print(url)

# 드라이버 호출 
driver_path = './webdriver/chromedriver.exe'
driver = webdriver.Chrome(driver_path, options=options)
driver.get(url)
time.sleep(1)

# 클릭 옵션 -> 위 함수 참조 
xpath = "/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/a"
ClickAction(xpath)

xpath = "/html/body/div[1]/div/div[3]/div[1]/div[2]/div[5]/ul/li[2]"
target = driver.find_element_by_xpath(xpath)
# target.click()

#yui_3_16_0_1_1588055722046_11184
imgs_list= list()
for num in range(1,10):

    img = driver.find_element_by_xpath(f'/html/body/div[1]/div/main/div/div/div[2]/div[{num}]/div/div/a')
    print(img)
    imgs_list.append(img.get_attribute("src"))


for idx, tmp in enumerate(imgs_list):

    urllib.request.urlretrieve( tmp, f'{idx}.jpg')
    print('이미지 생성')

# 테스트용 
time.sleep(5) 
driver.get('https://www.naver.com')

# 종료
driver.close()


