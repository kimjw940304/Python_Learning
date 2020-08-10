import tkinter.ttk as ttk  # combobox를 사용하기 위해 임포트해줘야함
from tkinter import *

root =Tk()
root.title("Nado GUI")
root.geometry("640x480")


# combobox는 리스트박스와 다르게 '창'을 열어서 여러개중 하나를 선택.  48min ~
# 즉, 콤보박스는 흔히 엑셀에서 '드롭다운' 메뉴라고 생각하면 된다.

values = [str(i)+"일" for i in range(1,32)]
# 콤보박스에서 height는 화살표를 선택시 한번에 보여지는 선택지의 갯수.
combobox = ttk.Combobox(root, height = 5 , value = values) 
combobox.pack()
# 콤보박스에 text를 입력가능 set()
combobox.set("최초 결제일")



# readonly 콤보박스 : 콤보박스란에 입력이 불가하고 선택만 가능함 ! (주로 사용)
# by, 끝에 state = "readonly" 추가!
readonly_combobox = ttk.Combobox(root, height = 10 , values = values, state ="readonly")
readonly_combobox.current(0)  # 선택 전 초기값을 0으로 세팅함.
readonly_combobox.pack()


def btncmd():
    # 콤보박스에서 선택한 값을 리턴  .get()
    print(combobox.get())
 

btn = Button(root, text = "선택", command=btncmd)
btn.pack()

root.mainloop()