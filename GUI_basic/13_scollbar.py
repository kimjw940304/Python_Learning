from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# scrollbar의 경우 scrollbar와 대상이 되는 wizet을 하나의 Frame내에 넣어두는게 편리하다.

# Frame생성
frame = Frame(root)
frame.pack()

# scrollbar 생성
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right",fill="y") # side 는 scrollbar를 frame 어디에 둘지 / fill은 bar사이즈를 y축에 매칭


# Listbox 생성
listbox = Listbox(frame, selectmode="extended", height=10,yscrollcommand=scrollbar.set)
# yscrollcommand-scrollbar.set()  .set을 빼면 스크롤내려도 다시 올라오는 오류발생 !!!!!! 

# yscrollcommad : scroll을 상하로 하면 y 좌우로 하면 x 이다 !
for i in range (1,32):
    listbox.insert(END,str(i)+"일") 
listbox.pack(side="left")

scrollbar.config(command=listbox.yview) 
# .config(command=listbox.yview) : 리스트박스의 y 축에 따라 스크롤바의 view가 변경되도록 매칭 필요 !!!!

root.mainloop()


'''
# 스크롤바 매칭오류 주의사항 2가지 ! #
(1) yscrollcommand=scrollbar.set  .set 누락 주의
(2) scrollbar.config(command=listbox.yview)   스크롤바 매칭 코드 누락 주의
'''
