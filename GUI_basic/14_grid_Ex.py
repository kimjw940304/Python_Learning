from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

'''
UI 개선 기능 정리
(1) sticky =N+E+W+S : 버튼을 동,서,남,북 방향으로 빈틈없이 늘려준다.
(2) padx = ? , pady =? : 버튼내부 text를 기준으로 상/하 공간을 지정해 버튼 사이즈 확장.
단, padx or pady 를 Button()내에 넣으면 버튼 자체의 사이즈 / grid() 내에 넣으면 버튼 사이의 간격!
(3) padx와 pady말고 width =? height=? 하면 버튼 사이즈 정확하게 지정도 가능 

'''

# 맨 윗줄
btn_f16 = Button(root,text="F16", padx=10, pady=10)
btn_f17 = Button(root,text="F17",padx=10, pady=10)
btn_f18 = Button(root,text="F18",padx=10, pady=10)
btn_f19 = Button(root,text="F19",padx=10, pady=10)

btn_f16.grid(row=0,column=0,sticky =N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0,column=1,sticky =N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0,column=2,sticky =N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0,column=3,sticky =N+E+W+S, padx=3, pady=3)

# clear 줄
btn_clear = Button(root,text="clear",padx=10, pady=10)
btn_equal = Button(root,text="=",padx=10, pady=10)
btn_div = Button(root,text="/",padx=10, pady=10)
btn_mul = Button(root,text="*",padx=10, pady=10)

btn_clear.grid(row=1,column=0,sticky =N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1,column=1,sticky =N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1,column=2,sticky =N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1,column=3,sticky =N+E+W+S, padx=3, pady=3)

# 7시작줄 
btn_7 = Button(root,text="7",padx=10, pady=10)
btn_8 = Button(root,text="8",padx=10, pady=10)
btn_9 = Button(root,text="9",padx=10, pady=10)
btn_sub = Button(root,text="-",padx=10, pady=10)

btn_7.grid(row=2,column=0,sticky =N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2,column=1,sticky =N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2,column=2,sticky =N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2,column=3,sticky =N+E+W+S, padx=3, pady=3)

# 4시작줄
btn_4 = Button(root,text="4",padx=10, pady=10)
btn_5 = Button(root,text="5",padx=10, pady=10)
btn_6 = Button(root,text="6",padx=10, pady=10)
btn_add = Button(root,text="+",padx=10, pady=10)

btn_4.grid(row=3,column=0,sticky =N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3,column=1,sticky =N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3,column=2,sticky =N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3,column=3,sticky =N+E+W+S, padx=3, pady=3)

# 1시작줄
btn_1 = Button(root,text="1",padx=10, pady=10)
btn_2 = Button(root,text="2",padx=10, pady=10)
btn_3 = Button(root,text="3",padx=10, pady=10)
btn_enter = Button(root,text="enter",padx=10, pady=10) # 세로로 합쳐짐 . row와 4,5에 걸쳐서

btn_1.grid(row=4,column=0,sticky =N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4,column=1,sticky =N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4,column=2,sticky =N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4,column=3, rowspan =2,sticky =N+E+W+S, padx=3, pady=3)  # rowspan =2 : "row (아래쪽으로)2개를 합치겠다.""

# 0시작줄
btn_0 = Button(root,text="0",padx=10, pady=10)   # 가로로 합쳐짐, column 0과 1에 걸쳐서
btn_point = Button(root,text=".",padx=10, pady=10)

btn_0.grid(row=5,column=0, columnspan=2,sticky =N+E+W+S, padx=3, pady=3)  # 세로로로 합쳐짐, column 0과 1에 걸쳐서
btn_point.grid(row=5,column=2,sticky =N+E+W+S, padx=3, pady=3)


root.mainloop()
