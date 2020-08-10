from tkinter import *

root =Tk()
root.title("Nado GUI")
root.geometry("640x480")

Label(root, text="< 메뉴를 선택하세요 >").pack()   # Label.pack()말고 이렇게 한번에 정의가능.

burger_var = IntVar() # 선택값을 int형으로 리턴한다.
btn_burgerSelect1 = Radiobutton(root, text="햄버거",value = 1, variable=burger_var)
btn_burgerSelect1.select() #기본선택 상태.
btn_burgerSelect2 = Radiobutton(root, text="치즈버거", value =2, variable=burger_var)
btn_burgerSelect3 = Radiobutton(root, text="게살버거",value =3, variable=burger_var)
######  variable 을 Variable로 쓰면 오류 !!!! 대소문자 잘 구분하기 #####
btn_burgerSelect1.pack()
btn_burgerSelect2.pack()
btn_burgerSelect3.pack()

# 리턴값을 int가 아닌 str 자체로도 가능
Label(root,text="< 음료를 선택하세요 >").pack()

drink_var = StringVar() # 리턴값을 문자열로 리턴.
btn_drink1 = Radiobutton(root, text="콜라", value ="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()

# Radiobutton : checkbutton(Yes OR No)과 다르게 여러개 중에 택일.
def btncmd():
    # 여러 선택지중 선택한 값을 출력 
    global menu 
    global drink
    if burger_var.get() == 1: #그냥 burger_var ==1 이라고 하면 오류남 !! 반드시 .get()
        menu = "햄버거"
    elif burger_var.get() == 2:
        menu = "치즈버거"
    elif burger_var.get() == 3:
        menu = "게살버거"

    if drink_var.get() == "콜라":
        drink = "콜라"
    elif drink_var.get() =="사이다":
        drink = "사이다"

    print("선택한 버거는 : ",menu, " 입니다.")
    print("선택한 음료는 : ",drink," 입니다.")
  
    
btn = Button(root, text = "선택", command=btncmd)
btn.pack()

root.mainloop()