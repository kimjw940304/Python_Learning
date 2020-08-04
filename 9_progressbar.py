import time
import tkinter.ttk as ttk  # combobox & progressbar 등을 사용하기 위해 임포트해줘야함
from tkinter import *

root =Tk()
root.title("Nado GUI")
root.geometry("640x480")


'''  progrssbar 단순 예시.
# progressbar : 진행상태 표시

# "Indeterminate" :왔다갔다하는 표시임  / : determinate :100%까지 차면 리셋
progressbar = ttk.Progressbar(root, maximum = 100, mode = "determinate") 
progressbar.start(10) # 10ms 마다 움직임
progressbar.pack() 

def btncmd():
    progressbar.stop()  # 작동 중지

btn = Button(root, text = "선택", command=btncmd)
btn.pack()
'''
p_var2 = DoubleVar()  # Double을 하면 Int와 달리 실수값으로 저장가능.
progressbar2= ttk.Progressbar(root, maximum=100, length =150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range (1,101):
        time.sleep(0.01)  #각 실행시 0.01초 대기

        p_var2.set(i)    #progressbar의 값 value를 설정 .set()
        progressbar2.update() # % 변화시 UI에 즉각 반영 .update()
        print(p_var2.get())

btn = Button(root,text='선택',command = btncmd2)
btn.pack()


root.mainloop()