from tkinter import *


root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

def create_new_file():
    print("새 파일을 생성합니다")

#                                          (1) Menu 기본 형태

menu = Menu(root) # root에 Menu를 생성.
# 기본 틀 익숙해지기.
menu_file = Menu(menu, tearoff=0)   
#  메뉴 버튼 생성. add_cascade()
menu.add_cascade(label="File", menu=menu_file)

# 메뉴 버튼에 선택지 추가하기 .add_command
menu_file.add_command(label="New File", command = create_new_file) #label : 버튼 이름
menu_file.add_command(label="New Window")
menu_file.add_separator()  # 구분자 추가 add_seperator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save", state = "disable") # state : 버튼 활성화 상태 
menu_file.add_separator()
menu_file.add_command(label="Exit", command = root.quit) # command : 버튼 명령(root.quit : 프로그램 종료)


#                                          (2) Menu (빈 값)
menu.add_cascade(label="Edit")

#                                          (3) Menu( Radiobutton 메뉴 추가 )
menu_lang = Menu(menu,tearoff=0)
# cascade() 는 반드시 menu_lang 값을 선언한 다음 추가해야함!
menu.add_cascade(label="Language", menu=menu_lang)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")

#                                          (4) Menu( Checkbutton 메뉴 추가 )
menu_view = Menu(menu, tearoff=0)
menu.add_cascade(label="View", menu=menu_view)
menu_view.add_checkbutton(label="Show Minimap")


root.config(menu=menu)
root.mainloop()