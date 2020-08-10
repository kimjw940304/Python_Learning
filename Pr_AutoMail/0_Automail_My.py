'''
Quiz. 동일한 내용의 메일에 유튜버 이름 정보만 변경하여 파일로 저장하는 프로그램을 작성하시오.
      
[ 조건 ]
1. 유튜버 이름은 '리스트'로 제공 (최소2명이상)
Ex. names = ["유튜버1","유튜버2","유튜버3"]

2. 파일명은 '유튜버 이름.txt' 로 저장
Ex. 나도코딩.txt 
'''

# 1. 메일을 보낼 유튜버 리스트 생성
names = []  # 메일을 보낼 유튜버 리스트
add_name = "yes"
while add_name == "yes": # 사용자가 수신자수 / 수신자 입력가능.
    names.append(input("메일을 보낼 유튜버 이름or채널명을 입력하시오:"))
    add_name = input("수신자를 추가하시겠습니까?(yes or no 를 입력) : ")

# 2. 동일한 내용 but 유튜버 이름만 바뀐 본문 작성 및 저장
file_name = ""
for receiver in names:
    # 동일한 내용 but 유튜버 이름만 바뀐 본문 작성
    contents_of_mail = ("안녕하세요?{0}님.\n(주)나도출판 편집자 나코입니다.\n현재 저희 출판사는 파이썬에 관한 주제로 책 출간을\
 기획 중입니다.\n{0}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.\n자세한 내용은 첨부드리는 제안서를\
 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.\n\n좋은 하루 보내세요^^\n감사합니다.\n\n- 나코 드림.".format(receiver))
    # 해당 내용을 포함한 파일 작성 및 저장
    with open(receiver+".txt",'w',encoding="utf8") as f:
        f.write(contents_of_mail)