'''
(1) 웹 크롤링 & 웹 스크래핑 차이점?

크롤링은 url에서 허용된 모든 자료를 가져오는 것.
스크래핑은 url에서 필요한 부분만 가져오는 것.

(2) VScode에서 HTML을 사용하려면 "open in browser"를 설치해야함.

(3) Requests 라이브러리
HTML문서를 불러올 수 있는 라이브러리. (pip install requests)

(4) User-Agent 확인 사이트
 https://www.whatismybrowser.com

(5) 이미지 파일을 write하는 방법 ! "wb"  &  .content 
    (img 파일은 text파일이 아닌 binary파일로 저장한다 !)

Ex. with open("movie{}.jpg".format(idx+1),"wb") as f:
    f.write(image_res.content)      

(6) .startswith("?")  함수
어떤 문자로 시작을 하는지 확인하는 함수이다.


(7) .strip() 함수
문자열의 양 끝에 존재하는 공백과 \n을 제거해주는 것
Ex.   data = column.get_text().strip() 
      print(data)

(8) .split("?") 함수
?로 구분된 것을 하나의 요소로 파악해서 list로 리턴하는 함수 
Ex. 
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실"
title_list = title.split("\t")
print(title_list)



(9) 웹의 어떤 table(row & column으로 이루어진)을 csv로 만드는 규칙
 1. table 데이터를 호출
 2. table의 모든 row데이터 호출 & 1 row씩 호출
 3. table의 모든 column데이터 호출 & 1 column씩 호출
 4. csv파일로 저장.

(10) list의 값들을 하나씩 csv파일 row에 입력해주는 코드
Ex.
f = open(filename,"w",encoding="utf8",newline="")
writer = csv.writer(f)
~~처리 코드~~
writer.writerow(리스트 이름)
'''