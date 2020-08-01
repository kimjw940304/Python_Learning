from tkinter import *

root =Tk()
root.title("Nado GUI")
root.geometry("640x480")

# combobox는 리스트박스와 다르게 '창'을 열어서 여러개중 하나를 선택. 


def btncmd():
    pass
 

btn = Button(root, text = "선택", command=btncmd)
btn.pack()

root.mainloop()