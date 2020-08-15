# 네이버금융 페이지의 코스피 시가총액 순위를 csv파일로 저장하는 프로그램.
import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

# (1) csv파일로 저장하는 코드  (12줄과 34줄이 필수 !!!)
filename = "시가총액1-200.csv"
# csv파일로 저장할때는 utf8 대신 utf-8-sig 로 encoding
f = open(filename,"w",encoding="utf-8-sig",newline="")
    # newline="" : 한줄(row)작성 후 enter를 치지 않도록 하는 코드 
writer = csv.writer(f)

# (2) title 넣어주기 
    
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실"
title_list = title.split("\t")
    # ctrl+v 한걸 보니 /t 으로 띄어쓰기된 규칙이있음 !
    # ★★.split(\t) 해서 tab으로 분리된 단위를 요소로하는 리스트를 생성!★★
writer.writerow(title_list)


# Url 가져오기 & Python으로 HTML문서 처리가능케 하기.
for page in range(1,5):
    res = requests.get(url+str(page))
    res.raise_for_status
    soup = BeautifulSoup(res.text,'lxml')

    # (3) 시가총액 자료 가져오기
        # table element의 class=type_2 안에있는 "body" element의 안에있는 모든 'tr' elment를 호출
    data_rows = soup.find("table", attrs = {"class":"type_2"}).find("tbody").find_all('tr')
    # (4) table의 모든 행(row) 데이터를 한 행씩 호출
    for row in data_rows:
        columns = row.find_all("td")
    # (★★)의미없는 공백을 제거하기 위한 코드(★★) 공식X 의미없는 코드들의 형태를 파악해서 그때그때
        if len(columns) <=1 :       # HTML문서상 의미없는 코드들은 td가 하나만 있었음!
            continue
    # (5) 각 행의 모든 열(column) 데이터를 한 열씩 호출
    #    불필요한 데이터는 없애기 위해 .strip()   : 문자열의 양 끝에 존재하는 공백과 \n을 제거해주는 것
        data = [column.get_text().strip() for column in columns]
        # 
        writer.writerow(data)
    