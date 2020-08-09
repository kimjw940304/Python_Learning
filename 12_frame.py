from tkinter import * 

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# pack(side=??)  side는 해당 UI의 위치를 설정가능.
Label(root, text="메뉴를 선택해 주세요").pack(side="top")
Button(root,text="주문하기").pack(side="bottom")


# 단순 Frame()
frame_burger = Frame(root, relief="solid", bd =1)   # relief : 테두리 모양 , bd : 테두리 굵기
# .pakc() 내부에 넣어서 frame의 위치, 형상 ,채우기 등을 설정가능.
frame_burger.pack(side="left",fill="both", expand="True")
# 버튼을 root가 아닌 frame 내부에 넣읗것이기에 frame_burger 
Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# 프레임에 라벨링하기 LabelFrame()
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side='right',fill="both",expand="True")

Button(frame_drink,text="콜라").pack()
Button(frame_drink,text="사이다").pack()

root.mainloop()
