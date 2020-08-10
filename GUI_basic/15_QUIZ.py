# QUIZ : tkinter 를 이용한 메모장 프로그램을 만드시오.

from tkinter import *
import os # Open할 파일이 있는지 없는지 여부를 check

root = Tk()
# 조건1. title : 제목없음 - Windowx 메모장
root.title("제목 없음 - Windows 메모장")
# 조건6. 프로그램 크기, 위치는 자유롭게 but 크기 조정은 가능
root.geometry("640x480")

# ★★★★★★★★★★★★★★★중요 !!★★★★★★★★★★★★★  #

# 열기, 저장 파일 이름
filename = "mynote.txt"

# 조건 3.1  '열기' : mynote.txt파일 내용을 열어서 보여주기
def file_open():
    # 우선, 열려는 파일 있는지 확인 (있으면 True, 없으면 False)
    if os.path.isfile(filename):
        # 파일있으면 read 해서 'file' 이라는 변수에 임시 저장.
        with open(filename, "r", encoding = "utf8") as file:
            # 파일을 불러오기 전에 기존 txt 창을 delect해줘야함
            txt.delete("1.0", END)
            # 해당 파일을 txt창에 insert 시켜준다 !
            txt.insert(END,file.read())


# 조건 3.2 '저장' : mynote.txt파일에 현재 내용 저장하기.
def file_save():
    with open(filename, "w", encoding = "utf8") as file:
        # txt의 1 line의 0 column 부터 END까지 값을 file에 .wirte한다.
        file.write(txt.get("1.0",END))

# ★★★★★★★★★★★★★★★중요 !!★★★★★★★★★★★★★  #


# 조건2. 메뉴: '파일', '편집', '서식', '보기', '도움말' 
menu = Menu(root)
# '파일' 메뉴 생성
menu_file = Menu(menu, tearoff=0)
menu.add_cascade(label="파일(F)", menu =menu_file)
#  '편집', '서식', '보기', '도움말' 는 ' 빈 메뉴' 로 생성
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")


# 조건3. '파일' 메뉴 내에 열기,저장, 끝내기 3개만 생성
menu_file.add_command(label="열기",command = file_open)
menu_file.add_command(label="저장",command = file_save)
menu_file.add_separator()   # 구분선 추가
# 조건 3.3 '끝내기' : 프로그램 종료 root.quit
menu_file.add_command(label="끝내기", command = root.quit) 

# 조건4. 프로그램 시작 시 본문은 비어 있는 상태의 메모칸 생성
# 조건7. 본문 우측에 상하 스크롤바 넣기.

# scrollbar 생성
scrollbar = Scrollbar(root)
scrollbar.pack(side="right",fill="y")

# text 입력창 생성
txt = Text(root, yscrollcommand=scrollbar.set)
# 스크롤바 상하 움직임에 따라 본문 view 매칭.
# ★ fill="both" 로 화면 전체를 frame으로 채우고 expand =True 로 사이즈 변경가능하게 작업 !  ★
txt.pack(side = "left", fill="both", expand=True)


#  ★ 아래 코드가 누락되면 '메뉴' 란이 화면에 보이지 않는다 !! 주의 ★
scrollbar.config(command = txt.yview)
root.config(menu=menu)
root.mainloop()