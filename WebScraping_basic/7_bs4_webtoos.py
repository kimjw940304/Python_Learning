import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml') # 불러온 HTML문서를 lxml파서?를 통해 Beautifulsoup객체로 생성

# 예제1. 네이버 웹툰 전체 목록 제목가져오기.

    # 첫번째만 리턴하는 find와 달리 모두를 리턴하는 .find_all
cartoons =soup.find_all("a",attrs = {"class":"title"})  
    # class속성이 title인 모든 "a" element를 반환

for cartoon in cartoons:
    print(cartoon.get_text())