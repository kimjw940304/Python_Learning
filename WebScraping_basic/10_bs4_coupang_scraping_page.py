# 예제) '쿠팡' 웹에서 노트북 구매하려는데, 내가 원하는 필터값에 해당하는 노트북만 찾기 프로그램

# ★★ 추가로 여러 페이지에 걸쳐서 스크래핑을 하는 방법 !★★

import requests
import re           # 정규식 사용을 위한 임포트
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}

# ★★ 추가로 여러 페이지에 걸쳐서 스크래핑을 하는 방법 !★★

# 간단하다 ! url page에 1~5부터 순차적으로 넣기만 하면 끝.
for i in range(1,6):  # 1~5페이지까지
    print("페이지:",i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)


    res = requests.get(url, headers = headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,"lxml")


    # (1) How? 정규식 사용
      
    items = soup.find_all("li", attrs = {"class":re.compile("^search-product")})
    print(items[0].find("div", attrs= {"class":"name"}).get_text())


    # (2) 전체 리스트 추출
    for item in items:

    # (3) 조건1: 광고가 붙은건 리스트에서 제외. 
        ad_badge = item.find("span", attrs = {"class":"ad-badge-text"})
        if ad_badge:
            # print(" < 광고 상품 제외합니다")
            continue  

    # (4) 조건2 : 애플 제품 제외
        # 제품명
        name = item.find("div", attrs = {"class":"name"}).get_text()
        if "Apple" in name:
            # print("< 애플 제품 제외합니다")
            continue
        
        # 가격 
        price = item.find("strong",attrs = {"class":"price-value"}).get_text()
        
        # 평점      
            # 단, 평점의 경우 위와 같이 작성하면 오류가 뜬다 (원인: 평점이 없는 상품이 있을 수 있음)

        rate = item.find("em", attrs={"class":"rating"})
        if rate:        # rate 값이 있을 경우
            rate = rate.get_text()
        else:           # rate 값이 없을 경우
            # print(" < 평점 없는 상품 제외합니다.")
            continue
        
        # 평점 갯수     
        rate_cnt = item.find("span", attrs = {"class":"rating-total-count"})
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()
            
            rate_cnt = rate_cnt[1:-1]
        else:
            # print((" < 평점 수 없는 상품 제외합니다."))
            continue 

        # 제품 구매 링크
        link = item.find("a", attrs = {"class":"search-product-link"})["href"]
        # product_link = link.a["href"]  # a element의 hfef 값을 호출한다.
        product_link = "https://www.coupang.com"+link


    # (5) 조건3 : 평점 4.5이상 되는 것만 조회 &  리뷰100개 이상 
        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
 
            print(f"제품명  : {name}")
            print(f"가격    : {price}")
            print(f"평점    : {rate}")
            print(f"평점 수 : {rate_cnt}")
            print(f"구매링크: {product_link}")
            print("-"*100)


           





    
    
    
