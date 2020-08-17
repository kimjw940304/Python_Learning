# 네이버 항공권예약 페이지에서 항공권 자동 조회 프로그램

from selenium import webdriver
# web에서 로딩타임이 끝나면 다음 코드를 실행시키는 모듈
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://flight.naver.com/flights/"
browser = webdriver.Chrome()
browser.maximize_window()   # 창 크기 최대화
browser.get(url)

# (1) 가는날 & 오는날 지정

# 가는 날 선택 클릭 ("가는날 선택"이라는 글자로 찾아보자.)
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27,28일 선택
    # 모든 달의 27일을 호출하고 첫번째(이번달) 27일을 선택한다.
browser.find_elements_by_link_text("27")[0].click()
browser.find_elements_by_link_text("28")[1].click()
'''
# 가는날 이번달 27일 & 오는날 다음달 28일
browser.find_elements_by_link_text("27")[0].click()
browser.find_elements_by_link_text("28")[1].click()
'''

# (2) 도착지 설정 
 
# 도착지 설정 버튼 클릭
browser.find_element_by_xpath("//*[@id='l_1']/div/div[2]/a[2]").click()
# "제주도" 선택
browser.find_element_by_xpath("//*[@id='l_1']/div/div[2]/div[2]/table[1]/tbody/tr[1]/td[1]/a").click()

# (3) 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# (4) 검색 첫번째 값 출력 (★로딩 타임 고려★) 
    # 웹을 10초간 대기 until Xpath값이 나올때 까지 (10초안에 나오면 바로 넘어감!)
try:
    elem = WebDriverWait(browser,10).until(EC.presence_of_element_located\
        ((By.XPATH,"//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 10초안에 정상적으로 로딩이 됐을 경우 출력
    print(elem.text)    
finally:
    # 실패시 브라우저 종료
    browser.quit()







