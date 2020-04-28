# selenium01_02.py
# 드라이버 팩 다운로드 경로 
# https://chromedriver.chromium.org/downloads

# pip install selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')

# 드라이버 가지고 오기 
driver_path = './webdriver/chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options= options)

# 드라이버에 진입할 경로 전달
driver.get("http://ihongss.com/webboard")


driver.execute_script("document.getElementsByName('email')[0].value='20191216'")
driver.execute_script("document.getElementsByName('pw')[0].value='20191216'")
driver.execute_script("document.getElementsByClassName('btn btn-primary')[0].click()")



# driver.find_element_by_name("email").send_keys('20191216')
# driver.find_element_by_name("pw").send_keys('20191216')
# driver.find_element_by_css_selector('#form1 > div:nth-child(4) > input').click()
# driver.find_element_by_xpath('//*[@id="form1"]/div[3]/input')


# pop창 띄우기 
time.sleep(3)
driver.execute_script('alert("hello")')

