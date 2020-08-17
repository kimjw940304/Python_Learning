# 반응형 웹을 스크랩하기.

from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.maximize_window()

# (1) 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)
'''
# 지정한 위치로 스크롤 내리기 (JavaScript)
    # 모니터(해상도) 높이인 1080 위치로 스크롤 다운
browser.execute_script("window.scrollTo(0,1080)") 
'''
# (2) 화면 가장 아래로 스크롤 다운
''' 
    # 문서 body의 Height만큼 스크롤 다운
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
'''
# (2-1) 2초에 한번씩 스크롤을 내림
interval = 2 

# (2-2) 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# (2-3) ★★반복 수행★★
while True:
        # 스크롤을 가장 아래로 내림.
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # 페이지 로딩 대기
    time.sleep(interval)
        # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
        # curr_height == pre_height 이면 더이상 가져올 자료가 없으니 탈출
    if curr_height == prev_height:
        break
    prev_height = curr_height

print("스크롤 완료")

# (3) 작업 준비가 된 페이지를 soup 객체로 만들기.
soup = BeautifulSoup(browser.page_source, 'lxml')

# (4) 스크랩 대상 지정
    # class가 여러개일 경우 list로 만들어준다.
movies = soup.find_all("div", attrs = {"class":"Vpfmgd"})
print(f"영화의 갯수는 :{len(movies)}개 입니다.")

# (5) 영화 정보 출력
for movie in movies:
    # 영화 제목
    title = movie.find("div", attrs = {"class":"WsMG1c nnK0zc"}).get_text()

    # 할인 전 가격
    original_price = movie.find("span", attrs = {"class":"SUZt4c djCuy"})
        
    if original_price: # 할인 전 가격이 있을 경우
        original_price = original_price.get_text()
    else:
        # print(title,"< 할인되지 않은 영화")
        continue
    
    # 할인 된 가격
    price = movie.find("span", attrs = {"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크 정보
    link = movie.find("a", attrs = {"class":"JC71ub"})["href"]
    link = "https://play.google.com"+link 

# (6) 영화 정보 출력
    print(f"영화 제목:{title}")
    print(f"할인 전 금액 :{original_price}")
    print(f"할인 후 금액 :{price}")
    print(f"링크 :{link}")
    print("-"*120)

