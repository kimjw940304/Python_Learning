from tkinter import * # __all__ 표시가 없기에 sub모듈은 따로 임포트해주지 않기에
from tkinter import filedialog # sub모듈인 filedialog를 따로 임포트 해줘야함 !
import tkinter.ttk as ttk  # Combobox , Progressbar사용을 위한 임포트
import tkinter.messagebox as msgbox

root = Tk()
root.title("")
# x(너비), y(너비) 값 변경 불가 (창 크기 변경불가 여부)
root.resizable(False,False) 

# 파일 추가 
def add_file():
    files = filedialog.askopenfilenames(title ="이미지 파일을 선택하세요",\
      filetypes = (("PNG 파일","*.png"), ("모든 파일","*.*")),\
       #  ★ r"디렉토리" 해주면 탈출문자 없이도 \ 를 그대로 표시가능하다 !!!  ★
      initialdir = r"C:\Users\김재원\Pictures")
    # 사용자가 선택한 파일 목록
    for file in files:
      list_file.insert(END,file)

# 선택 삭제 
def del_file():
    #  ★ delete는 Index 지정으로 삭제하는데, 앞에서부터 지우면 원하는 결과 X 뒤에서 부터 삭제 ★ 
    # 현재 선택한 값들의 index 값을 리턴해주는 함수 .curselection()
    for index in reversed(list_file.curselection()):
      list_file.delete(index)


# 저장 경로(폴더 선택)
def browse_dest_path():
  # .askdirectory() "폴더 찾기" 기능 제공 함수 리턴값은 선택한 디렉토리값
  folder_selected = filedialog.askdirectory()
  if folder_selected == "": #사용자가 폴더 선택없이 취소를 누를경우
    return
  # 우선 기존 선택했던 경로 삭제
  txt_dest_path.delete(0,END)
  # 선택한 경로를 입력
  txt_dest_path.insert(0,folder_selected)


# 시작 
def start():
  # 각 옵션들 값을 확인

  # 파일 목록 확인
  if list_file.size() == 0 : # 선택된 파일이 없을 경우
    msgbox.showwarning("경고", "이미지 파일을 추가하세요")
    return

  # 저장 경로 확인
  if len(txt_dest_path.get()) == 0 : # 저장 경로 미선택시
    msgbox.showwarning("경고", "저장경로를 선택하세요")
    return













# (1) 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill ="x", padx=5, pady=5)

btn_add_file = Button(file_frame,padx=5, pady=5, width= 12, text="파일추가", command = add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame,padx=5, pady=5, width= 12, text="선택삭제", command= del_file)
btn_del_file.pack(side="right")

# (2) 리스트 프레임
list_frame =Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)  # fill="both"로 frame이 상하좌우 꽉차게끔 작업.

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
  # fill="both" 해당 박스가 상하좌우 꽉 매우게끔 ! & expand =True 로 사이즈 변경가능
list_file.pack(side="left", fill ="both", expand=True) 
  # 스크롤바와 박스 y축 view 연동 
scrollbar.config(command =list_file.yview)


# (3) 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5)

  # 저장경로 창은 한줄이기에 Text말고 Entry로 작성.
txt_dest_path = Entry(path_frame)
  # 저장경로 창은 x축으로 확장이기에 fill="x" 
  # ★ 칸의 세로 높이 지정 ipady (inner pad) frame내부라 pady 로 하면 반영 안된다!! ★
txt_dest_path.pack(side="left", fill="x",expand=True, padx=5, pady=5, ipady =4)

btn_dest_path = Button(path_frame, text="찾아보기", width = 10, command = browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)


#  (4) 옵션 프레임
option_frame = LabelFrame(root, text="옵션")
option_frame.pack(fill="both", padx=5, pady=5)

  #(4.1) 가로 넓이 옵션
    # 가로 넓이 Label
lbl_width = Label(option_frame, text="가로넓이", width=8)
lbl_width.pack(side="left")
    # 가로 넓이 Combobox
opt_width = ["원본유지", "1024", "800", "640"]  # 콤보박스 값은 '리스트' 로 저장해둔다.
cmb_width = ttk.Combobox(option_frame,state="readonly", values= opt_width, width =10)
cmb_width.current(0) # 첫값은 첫 선택지로 디폴트값 설정
cmb_width.pack(side="left", padx=5, pady=5)

  #(4.2) 간격 옵션
    # 간격 옵션 Label
lbl_space = Label(option_frame, text="간격", width = 8)   
lbl_space.pack(side="left", padx=5, pady=5)
    # 간격 옵션 Combobox
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(option_frame, state ="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

  #(4.3) 파일 포맷 옵션
    # 파일 포맷 Label
lbl_format = Label(option_frame, text="포맷", width =8)
lbl_format.pack(side="left", padx=5, pady=5)
    # 파일 포맷 Combobox
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(option_frame, state = "readonly", values = opt_format)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

#  (5) 진행 상황 Progressbar
frame_progress = LabelFrame(root, text = "진행상황")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum = 100, variable = p_var )
progress_bar.pack(fill="x", padx=5, pady=5,)


#  (6) 시작/닫기 프레임
frame_run = Frame(root)
frame_run.pack(fill="x")

btn_close = Button(frame_run, text = "닫기", padx = 5 , pady = 5, width = 12, command = root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, text = "시작", padx = 5 , pady = 5, width = 12, command = start)
btn_start.pack(side="right", padx=5, pady=5)


root.mainloop()