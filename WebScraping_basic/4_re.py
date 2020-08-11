'''
[  정규식(RE) : Regular Expression  ]
 What?
    틀,형태,포맷 등이 정해져있는 데이터(값)
    Ex. 주민등록번호 , 이메일주소, 차량번호 등..

 Why?
    반복적인 작업을 설정한 특정한 포맷내에서 동작하게 할떄 쓴다.

 How?
 (1) 원하는 패턴 입력 
    p = re.compile("원하는 형태")
 (2) 비교 구문 작성
    m = p.match("비교할 문자열")
    m = p.search("비교할 문자열")
    m = p.findall("비교할 문자열")

'''
# . (ca.e)  : '하나의 문자'를 의미 Ex. care, cafe, case(O) | caffe(x)
# ^ (^de)   : 문자열의 '시작'      Ex. desk, destination (O) | fade (x)
# $ (se$)   : 문자열의 "끝"        Ex. case, base (O) | face(x)

import re

# (1) p : pattern & 차량 번호판의 일부분만 알고 있는경우 모든 경우의 수 도출하는 예제.

    # 방식1

p = re.compile("ca.e")   # ca?e 의 pattern을 다수 생성.
m = p.match("case")      # pattern 내에서 .match("?") 와 일치하는 값을 리턴받음.

    # IF) 매칭O: 매칭값을 리턴 & 매칭X : Error발생 
if m:                    
    print(m.group())
else:
    print("매칭되지 않음.")


    # 방식2  .match() : 주어진 '문자열의 처음부터' 일치하는지 확인
    
def print_match(m):
    if m :
        print(m.group())                    # 일치하는 문자열 리턴
        print("m.string:", m.string)        # 입력받은 문자열 리턴
        print("m.start():",m.start())       # 일치하는 문자열의 시작 Index 리턴
        print("m.end():",m.end())           # 일치하는 문자열의 끝 Index 리턴
        print("m.span():",m.span())         # 일치하는 문자열의 시작 & 끝 Index 리턴
    else:
        print("매칭되지 않음")

p = re.compile("ca.e")

m = p.match("care") #단,careless 를 입력해도 매칭됨 why? match의 특성.
print_match(m)

    # 방식3  .search() : 주어진 '문자열 중에' 일치하는게 있는지 확인
m = p.search("good care") # 문자열 중에 care가 있으니 ok
print_match(m)
 
    # 방식4. .findall() : 일치하는 모든 것을 리스트 형태로 반환
lst = p.findall("good care cafe")
print(lst)