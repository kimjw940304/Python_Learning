from tkinter import *

root = Tk()
root.title("Nado GUI") 
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file = "C:\\Users\\김재원\\Desktop\\PythonWorkspace\\GUI_Learning_PROJECT\\img.png")
label2 = Label(root,image=photo)
label2.pack()

# 버튼 클릭시 label1 text가 변경되는 기능

# config(변경속성:변경할 값) 속성값을 변경하는것.

def change():
    label1.config(text="또 만나요")  
    # photo2는 함수 내에 선언됐기에 global로 '전역변수' 로 선언을 해야만 반영이 된다 !
    # 그렇지 않으면, Garbage Collection 에 의해 삭제됨.
    global photo2
    photo2 = PhotoImage(file = "C:\\Users\\김재원\\Desktop\\PythonWorkspace\\GUI_Learning_PROJECT\\img2.png")
    label2.config(image=photo2) 

btn = Button(root,text="클릭",command=change)
btn.pack()

root.mainloop()  # mainloop() 는 윈도우를 종료시키는 명령이 있기전까지 화면을 유지하는 함수.
