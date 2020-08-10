
(1) 디렉토리 표시할때 탈출문자 쓰지 않는방법 r"디렉토리"
Ex.  initialdir = r"C:\Users\김재원\Pictures"

(2) '파일 추가' 기능을 사용하기 위한 모듈

from tkinter import filedialog # sub모듈인 filedialog를 따로 임포트 해줘야함 !

(3) "파일 삭제" 기능 구현시 뒷 순서부터 삭제하기 !
#★ delete는 Index 지정으로 삭제하는데, 앞에서부터 지우면 원하는 결과 X 뒤에서 부터 삭제 ★

(4) 두 리스트를 같은 index끼리 묶어서 하나의 리스트로 만들고 합치는 함수 .zip()
# 단, zip() 리턴 자료형은 zip 자료형이기에 list(zip()) 으로 해줘야함.
kor = ["사과","바나나","오렌지"]
eng = ["apple","banana","oragne"]
print(list(zip(kor,eng)))

# 반대로, zip되어 있는것을 부니 할 수 있음. .zip(*분리할리스트)
ziped = [('사과', 'apple'), ('바나나', 'banana'), ('오렌지', 'oragne')]
print(list(zip(*ziped)))