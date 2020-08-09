from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# 쌓아올리는 .pack() 과 다르게 .grid(row=?,colum=?)를 쓰면 보다 디테일하게 위치 지정가능

btn1 = Button(root, text="버튼1")
btn2 = Button(root, text="버튼2") 
# btn1.pack()
# btn2.pack()
btn1.grid(row=0,column=0)
btn2.grid(row=1,column=1)




root.mainloop()
