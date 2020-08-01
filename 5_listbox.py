from tkinter import *

root =Tk()
root.title("Nado GUI")
root.geometry("640x480")

# Listbox 생성 Listbox
listbox = Listbox(root, selectmode="extended", height=0) 
# extended 여러개 선택가능 single : 여러개 선택가능
# height = 0 : 리스트를 한번에 다 표시 1 ~  : 한번에 표시할 갯수 (화살표로 확인가능)
listbox.insert(0,"사과") #리스트 첫번째에 삽입
listbox.insert(1,"딸기") 
listbox.insert(2,"바나나")
listbox.insert(END,"수박") #리스트 마지막순서에 추가.
listbox.insert(END<"포도")
listbox.pack()

def btncmd():
    # 선택사항 삭제   .delete()
    #listbox.delete(END) # 맨 마지막항목 삭제
    #listbox.delete(0)    # 맨 첫번째 항목 삭제
    
    # 갯수확인 .size()
    #print("리시트에는", listbox.size(),"개가 있어요")

    # 항목 확인   .get()
    #print("1~3까지의 항목:", listbox.get(0,2))

    # 선택된 항목 확인( 인덱스로 반환 )   .curselection()
    print("선택된 항목은 : ",listbox.curselection(),"입니다")

btn = Button(root, text = "선택", command=btncmd)
btn.pack()

root.mainloop()