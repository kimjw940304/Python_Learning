from tkinter import *

root = Tk()
root.title("Nado GUI") 
root.geometry("640x480")

btn1 = Button(root, text="버튼1")  # 버튼 생성
btn1.pack()  # 버튼명.pack() 을 해줘야 윈도우에 버튼이 display됨.

# padx =? (버튼 좌우 여백 ) pady =? (버튼 위아래 여백)  *여백 = 버튼명부터 좌우/세로 여백
btn2 = Button(root,padx= 5 , pady=10, text="버튼2")  
btn2.pack() 

btn3 = Button(root,padx= 10 , pady=5, text="버튼3")
btn3.pack() 

# width =? (버튼 가로폭) height =? (버튼 세로폭)   * 버튼 사이즈 고정.
btn4 = Button(root,width= 10 , height=3, text="버튼4")
btn4.pack() 

# fg : foreground (글자색) / bg: background(배경색) 
btn5 = Button(root, fg="red",bg="yellow",text="버튼5")
btn5.pack() 

# 이미지를 통해 button 생성 image
photo = PhotoImage(file="C:\\Users\\김재원\\Desktop\\PythonWorkspace\\GUI_Learning_PROJECT\\img.png")  
# 디렉토리 표시때는 \를 표시하기 위해 탈출문자 \\ 두개로 기입해야함.
# photoImage(file="파일경로")
btn6= Button(root, image=photo)
btn6.pack() 

# 버튼 클릭시 동작 command
def btncmd():
    print("버튼이 클릭되었습니다")

btn7 = Button(root, text="동작하는 버튼",command=btncmd)  #버튼 입력시 btncmd 함수가 실행.
btn7.pack()





root.mainloop()  # mainloop() 는 윈도우를 종료시키는 명령이 있기전까지 화면을 유지하는 함수.
