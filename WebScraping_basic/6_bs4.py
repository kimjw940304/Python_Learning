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
print(soup.title)             # HTML파일에서 title 스팬을 갖는 값을 리턴.
print(soup.title.get_text())  # .get_text() 로 해당 span의 내용만 리턴가능.  
print(soup.a)                 # 단, 이 방식은 soup객체에서 처음 발견되는 a 객체 리턴
print(soup.a.attrs)           # attrs : attributes (a element의 "속성값"  리턴)
print(soup.a["href"])         # a element의 href 속성값 리턴  (이건 잘 안쓰는 방식.)

# (3-1) 일반적으로 HTML구조를 잘 모를때 쓰는 방식   .find() 
print(soup.find("a"))       # soup객체에서 첫 a element를 찾는다. 뒤에 추가 속성조건 추가가능.
print(soup.find("a", attrs={"class":"Nbtn_upload"}))

# (4) 같은 부모밑에 있는 다른 형제 불러오기 .next_sibling / .previous_sibling
rank1 = soup.find("li", attrs={"class":"rank01"})  # li태그에서 rank01 이라는 클래스 속성값
print(rank1.a.get_text())
rank2 = rank1.next_sibling.next_sibling     # 한번 써서 안나오면 두번 쓰면된다. (빈칸있을 수 있어서)
print(rank2.a.get_text())

# (5) 자식으로부터 부모단으로 올라가기 .parent
print(rank1.parent)

# (6) next_sibling보다 정확한 .find_next_sibling()  빈칸은 띄우고 서치해줌.
rank2 = rank1.find_next_sibling("li")  # li 태그를 찾고 rank1 클래스 다음 rank2 클래스 를 찾아줌.
print(rank2.a.get_text())

# (7) 같은 부모밑에 있는 모든 자식들 불러오기 .find_next_siblings  
print(rank1.find_next_siblings("li"))

# (8) 특정 태그에서 특정 텍스트를 포함한 값을 리턴 .find("태그",text="?")
webtoon = soup.find("a",text="복학왕-304화 광어인간 2화")
print(webtoon)
