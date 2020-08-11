'''처음할 경우 설치 패키지
pip install beautifulsoup4  # 
pip install lxml            #
'''

import requests
from bs4 import BeautifulSoup

# (1) 불러올 HTML문서의 url 입력.
url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()          # requests.get() 다음에는 항상 넣어서 오류 발생여부 체크!!

# (2) 불러온 HTML문서를 lxml파서?를 통해 Beautifulsoup객체로 생성
soup = BeautifulSoup(res.text, "lxml")  

# # (3) BeautifulSoup 객체로 만들었기에 파이썬코드로 HTML이 작동이 가능함!
# print(soup.title)             # HTML파일에서 title 스팬을 갖는 값을 리턴.
# print(soup.title.get_text())  # .get_text() 로 해당 span의 내용만 리턴가능.  
# print(soup.a)                 # 단, 이 방식은 soup객체에서 처음 발견되는 a 객체 리턴
# print(soup.a.attrs)           # attrs : attributes (a element의 "속성값" 리턴)
# print(soup.a["href"])         # a element의 href 속성값 리턴  (이건 잘 안쓰는 방식.)

# (3-1) 일반적으로 HTML구조를 잘 모를때 쓰는 방식   .find() 
print(soup.find("a"))       # soup객체에서 첫 a element를 찾는다. 뒤에 추가 속성조건 추가가능.
print(soup.find("a", attrs={"class":"Nbtn_upload"}))