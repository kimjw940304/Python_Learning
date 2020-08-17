# 동적 page에 대한 웹 스크래핑 (Ex. 스크롤링 했을때 페이지가 업로드 되는 인스타그램 같은 페이지)

# 구글 무비 "인기 차트" 에서 "할인" 중인 영화 리스트만 뽑아오는 프로그램

import requests
from bs4 import BeautifulSoup

# (1) 스크래핑 대상 url 및 soup 객체 생성

# ★header선언으로 한국에서 접속하는걸 보여줘야 한글 리스트를 리턴해주니까!!★
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
    ,"Accept-Language":"ko-KR,Ko"
    }

url = "https://play.google.com/store/movies/top"
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


# (2) 스크랩 대상 지정 
movies = soup.find_all("div", attrs = {"class":"ImZGtf mpg5gc"})

# 웹을 확인해보면 10개만 뜬다 why? 웹에서 스크롤하면 10개 단위로 추가로 보여주고 있는걸 확인가능 !!
print(len(movies))

# (3) 제목 리스트 호출
for movie in movies:
    title = movie.find("div", attrs = {"class":"WsMG1c nnK0zc"}).get_text()
    print(title)

 