import requests
from bs4 import BeautifulSoup

url =  "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

예제1) 특정 만화의 제목 및 링크정보 리턴받기.
cartoons = soup.find_all("td", attrs = {"class":"title"})
'''
    # 제목 정보.
title = cartoons[0].a.get_text()
print(title)
    # 링크 정보 
link = cartoons[0].a["href"]        # a태그 내의 href 속성값을 리턴!
    # FUll링크 정보는 THML에서 마우스를 올려두면 나오기에 앞에 추가한다
print("https://comic.naver.com"+link)                        
 '''   
    # 제목/링크 정보를 모두 불러오기
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = cartoon.a["href"]
    print("제목  :"+title)
    print("링크  :"+"https://comic.naver.com"+link)

# 예제2) 만화들의 평점을 불러와서 평균값 계산
total_rates = 0
cartoons = soup.find_all("div", attrs = {"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    total_rates += float(rate)
print("평균 점수:",(total_rates/len(cartoons)))