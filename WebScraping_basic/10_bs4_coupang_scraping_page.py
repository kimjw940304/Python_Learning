# 예제) '쿠팡' 웹에서 노트북 구매하려는데, 내가 원하는 필터값에 해당하는 노트북만 찾기 프로그램

# ★★ 추가로 여러 페이지에 걸쳐서 스크래핑을 하는 방법 !★★

import requests
import re           # 정규식 사용을 위한 임포트
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
# "호스트로부터 응답이 없어 연결이X" ~ 내용이 뜨면 User-Agent를 직접 주는 방식을 추가해보자.
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
#  이 경우 .get() 에 hearders 를 추가해줘야함 !
res = requests.get(url, headers = headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")


# (1) How? 정규식 사용

    # search-product로 '시작'하는 class속성을 갖는 li element 반환
items = soup.find_all("li", attrs = {"class":re.compile("^search-product")})
    # items의 많은 정보들 중에서 name 클래스를 갖는 첫번째 div element 반환
print(items[0].find("div", attrs= {"class":"name"}).get_text())


# (2) 전체 리스트 추출
for item in items:

# (3) 조건1: 광고가 붙은건 리스트에서 제외. 
    ad_badge = item.find("span", attrs = {"class":"ad-badge-text"})
    if ad_badge:
        print(" < 광고 상품 제외합니다")
        continue  # ★광고 상품이면 바로 다음 item[] 으로 넘어가게 for문에서 아래 코드를 넘어뛴다.★

# (4) 조건2 : 애플 제품 제외
    # 제품명
    name = item.find("div", attrs = {"class":"name"}).get_text()
    if "Apple" in name:
        print("< 애플 제품 제외합니다")
        continue
    
    # 가격 
    price = item.find("strong",attrs = {"class":"price-value"}).get_text()
    
    # 평점      
        # star = item.find("em", attrs={"class":"rating"}).get_text()
        # print(star)
        # 단, 평점의 경우 위와 같이 작성하면 오류가 뜬다 (원인: 평점이 없는 상품이 있을 수 있음)

    rate = item.find("em", attrs={"class":"rating"}).get_text()
    if rate:        # rate 값이 있을 경우
        rate = rate
    else:           # rate 값이 없을 경우
        print(" < 평점 없는 상품 제외합니다.")
        continue
    
    # 평점 갯수     
    rate_cnt = item.find("span", attrs = {"class":"rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        # rate 값이 (??) 처럼 ()로 둘러 쌓여있길래 재가공 필요
        rate_cnt = rate_cnt[1:-1]
    else:
        print((" < 평점 수 없는 상품 제외합니다."))
        continue


# (5) 조건3 : 평점 4.5이상 되는 것만 조회 &  리뷰50개 이상
    if float(rate) >= 4.5 and int(rate_cnt) >= 50:

        print("제품명:",name)
        print("가격:",price,"원")
        print("평점:",rate)
        print("평점 수 :",rate_cnt)



    

    
    
    
