from tkinter import *
# 별도 import필요
import tkinter.messagebox as msgbox 

root =Tk()
root.title("Nado GUI")
root.geometry("640x480")

# messagebox 는 '에러메시지' 등과 같은 팝업을 보여줄때 사용가능.

# .showinfo()  
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다")
# .showwaning()
def warn():
    msgbox.showwarning("경고","해당 좌석은 매진되었습니다")

# .showerror()
def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다")

# .askokcancel()  사용자가 OK or Cancel 둘중 하나를 선택가능.
def okcancel():
    msgbox.askokcancel("확인/취소","해당 좌석은 유아동반석입니다. 예매하시겠습니까?")

# .askretrycancel() 
def retrycancel():
    msgbox.askretrycancel("재시도/취소","일시적 오류 발생, 다시 시도하겠습니까?") 

# .yesno()
def yesno():
    msgbox.askyesno("예/아니오","해당 좌석은 역방향입니다. 예매하시겠습니까?")

# .yesnocancel()
def yesnocancel():
    response = msgbox.askyesnocancel(title=None, \
        message="예매 내역이 저장되지 않았습니다\n 저장 후 프록램 종료하시겠습니까?")
# 네 : 저장 후 종료
# 아니오 :저장 하지 않고 종료
# 취소 : 프로그램 종료 취소( 현재 화면에서 계속 작업)
    print("응답:", response) #True,False,None -> 예 1, 아니오 0, 그외 None
    if response == 1: 
        print("예")
    elif response ==0:
        print("아니오")
    else:
        print("취소")



Button(root, command=info, text = "알림").pack()
Button(root, command=warn, text = "경고").pack()
Button(root, command=error, text = "에러").pack()
Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text = "에 아니오").pack() 
Button(root, command=yesnocancel, text = "에 아니오 취소").pack()

 

root.mainloop()
 
