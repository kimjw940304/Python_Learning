# 네이버 항공권예약 페이지에서 항공권 자동 조회 프로그램

from selenium import webdriver

url = "https://flight.naver.com/flights/"
browser = webdriver.Chrome()
browser.maximize_window()   # 창 크기 최대화
browser.get(url)

# (1) 가는날 지정

# (2) 오는날 지정

