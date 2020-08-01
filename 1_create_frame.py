'''
<  GUI 프로그래밍 (Graphical User Interface) >

# What? 
 눈으로 볼 수 있는 프로그램으로 (버튼, 텍스트 박스 ,레이블 등으로 구성 )

# How?
 tkinter Liabrary를 활용


 cf) Tk (toolkit)? 
    툴킷이란 특정목적을 수행하기 위해 필요한 도구들을 제공하는것.

'''
from tkinter import *

root = Tk()
root.title("Nado GUI") 
root.geometry("640x480")  # x 를 대문자 X로 하면 오류난다.!!!

root.mainloop()  # mainloop() 는 윈도우를 종료시키는 명령이 있기전까지 화면을 유지하는 함수.
