from tkinter import *

root =Tk()
root.title("Nado GUI")
root.geometry("640x480")

# text를 입력할 수 있는 공간 생성 Text
txt = Text(root, width=30, height=5)
txt.pack()
# text박스에 기본값을 입력 insert    
txt.insert(END,"글자를 입력하세요")  # END는 그 글자를 끝에 넣어둔다는 의미

# Entry창 (Entry란? Enter를 입력할 수 없는 창으로 ID/PW와 같이 Enter입력 불가칸 생성시 활용)
e= Entry(root,width=30)
e.pack()
e.insert(END,"아이디를 입력하세요")

# 버튼 클릭시 text값을 print하는 버튼을 생성
def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))  #"1.0" : 1: 첫번째 line, 0: 0번째 colum , END 끝까지.
    print(e.get()) #entry 는 한줄이기에 get() 만 써줘도 괜찮다.
    # 내용 삭제
    txt.delete("1.0",END)
    e.delete(0,END)   # delete할때는 entry라도 0,END를 써줘야함 !!!

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()