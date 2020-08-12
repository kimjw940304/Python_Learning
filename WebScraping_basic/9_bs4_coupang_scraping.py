# 예제) '쿠팡' 웹에서 노트북 구매하려는데, 내가 원하는 필터값에 해당하는 노트북만 찾기 프로그램

import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")