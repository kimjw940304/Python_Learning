'''
* 유니코드(Unicode)
1. What?
"국제표준 문자표"

국제적으로 전세계 언어를 모두 표시할 수 있는 표준 코드 (테이블)

2. Why?
1byte 안에 임의대로 알파벳or숫자 대신 자국어를 할당하기 위해

3. How?
유니코드 테이블을 참조 .

한글의 경우 UTF-8 이 유니코드를 '인코딩 방식'이다. 

'''
score_file = open("score.txt",'w', encoding="utf8")  # encoding ="utf8" 의 경우 한글 파일을 작성할때 추가해주면 오류가 나는 것을 방지해준다.
print("수학:0", file=score_file)
print("코딩:100", file=score_file)
score_file.close()

# score_file = open("score.txt",'a', encoding="utf8") 
# score_file.write("과학:80")
# score_file.write("\n영어:80")  #.write()의 경우 줄바꿈을 하지 않는다. 따라서 줄바꿈 \n을 해줘함
# score_file.close()
'''       #   read() 함수로 파일을 읽어온다. #

score_file = open("score.txt",'r', encoding="utf8")  
print(score_file.read())  # read() 는 파일 전체를 읽어온다.

'''
'''       # readline() 으로 한줄씩 파일을 읽어온다.# 

score_file = open("score.txt",'r', encoding="utf8")  
print(score_file.readline(),end='')  # readline() 은 줄별로 한줄 만 읽고, 커서는 다음 줄로 이동
print(score_file.readline(),end='')  # readline() 은 줄별로 한줄 만 읽고, 커서는 다음 줄로 이동

'''
# # line이 없을때까지 한줄씩 read
# score_file = open("score.txt",'r', encoding="utf8") 
# while True:
#     line = score_file.readline()
#     if not line:  # line의 값이 없을경우
#         break   # line이 없을 경우 while 반복문 자체를 탈출한다.
#     print(line,end='')
# score_file.close()

# # readlines() 파일 전체를 read해서 list형태로 저장
# score_file = open("score.txt",'r', encoding="utf8") 
# lines = score_file.readlines()  # 파일을 read하고 list값으 리턴
# for line in lines:
#     print(line,end='')