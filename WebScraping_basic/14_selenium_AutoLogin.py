# 웹에 접근하여 자동으로 로그인하는 프로그램

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# (1) 브라우저 객체 생성 & 접근할 url에 접근
browser = webdriver.Chrome()
url = "http://naver.com"
browser.get(url)

# (2) 로그인 버튼 클릭
login_elem = browser.find_element_by_class_name("link_login")
login_elem.click()

# (3) ID입력
ID_elem = browser.find_element_by_id("id")
ID_elem.send_keys("ID입력")

# (4) Password입력
PW_elem = browser.find_element_by_id("pw")
PW_elem.send_keys("PW입력")

# (5) 로그인 클릭
Login_btn = browser.find_element_by_xpath("//*[@id='log.login']").click()

# HTML 정보 출력
print(browser.page_source)




