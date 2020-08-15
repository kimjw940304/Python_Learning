'''selenium사용 설치파일
1. pip install selenium
2. 활용 웹 드라이버 설치
    (1) 웹 버전 확인 
        - 검색창에  chrome://version 입력
    (2) 드라이버 설치
        - 구글에 chromedriver 입력 후 사이트 접속
        - 버전에 맞는 드라이버 설치.
        - 파이썬설치 폴더에 압축해제
'''

# 크룸 드라이버가 파이썬 프로그램과 다른 경로에 설치되어있으면
# 따로 ""안에 설치된 디렉토리를 써줘야한다. 
# ex. .chrome("c:/downloads/chromedriver.exe")

from selenium import webdriver
# (1) chrome 웹드라이버 객체 생성
browser = webdriver.Chrome()
# (2) 브라우저에서 특정 url로 접속
browser.get("http://naver.com")
 
# (3) 각종 웹 제어 코드
    # class 또는 id 속성으로 element를 find하는법
    # 복수의 값을 갖고자하면 elements 
elem = browser.find_element_by_class_name("클래스명")
elem = browser.find_element_by_id("id명")

    # xpath로 간단하게 find가능
elem = browser.find_element_by_xpath("xpath copy한 값 붙여넣기")

    # attr값을 갖고오는 방법
elem.get_attribute("href")
 
    # 이전페이지 / 앞 페이지 /클릭 / 새로고침 
browser.back()
browser.forward()
elem.click()
browser.refresh()
    # 특정 elem에 값을 입력하고 & enter
from selenium.webdriver.common.keys import Keys  # Enter를 하기 위한 임포트
elem.send_keys("나도 코딩")  # elem에 특정값을 입력
elem.send.keys(Keys.ENTER)  # elem를 Enter하는 기능. 

    # browser 종료
browser.close()     #해당 탭만 닫기
browser.quit()      #브라우저 자체를 종료