from tkinter import *

root =Tk()
root.title("Nado GUI")
root.geometry("640x480")

# checkBox 만들기 Checkbutton() , Intvar()
# 함수이름은 Checkbox가 아니고 Checkbutton임 헷갈림 주의.

chkvar = IntVar()  #  checkbox 선택 여부를 int형으로 값으로 리턴.
chkbtn = Checkbutton(root, text = "오늘 하루 보지 않기", variable=chkvar)  # variable 이 중요!
chkbtn.select() # 선택 or 디폴트값 : 선택
#chkbox.deselect() # 선택 해제 or 디폴트 선택 해제
chkbtn.pack()


chkvar2= IntVar()
chkbtn2 =Checkbutton(root, text = "일주일동안 보지 않기", variable = chkvar2)
chkbtn2.pack()

def btncmd():
    # checkbox 선택 여부 출력 0: 체크 해제  1: 체크 선택
    print(chkvar.get())  
    print(chkvar2.get()) 
 

btn = Button(root, text = "선택", command=btncmd)
btn.pack()

root.mainloop()