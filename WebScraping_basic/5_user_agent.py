'''
User Agent

 What? 
    웹에서 웹에 접근하는 대상을 파악하기 위한 방식.
 Why?
    PC 웹으로 접근인지, 폰 app으로 접근인지, 기타 인지 확인용
 How?
    웹에 접근시 접근자가 제공하는 User agent를 파악 (header에 포함되어 있음)
'''

# 임으로 웹에 접근시 headers부분에 User-Agent 값을 입력해두면 해당 User-Agent로 접근이 가능!! (우회방식)
import requests
url = "http://nadocoding.tistory.com"
    # https://www.whatismybrowser.com 에서 복사한 접근시 사용하고자 하는 User-Agent값 입력
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
res = requests.get(url, headers=headers) 
res.raise_for_status() # url불러오다 오류 발생시 프로그램 종료
with open("nadocoding.html","w",encoding="utf8") as f:
    f.write(res.text)  # url에 있는 값을 txt로 저장.
