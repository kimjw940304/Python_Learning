'''      # Pickle 모듈  #
1. What? 
'텍스트(txt)' 이외의 자료형을 '파일'로 저장하는 모듈

2. why?
'리스트'나 '클래스'같은 '텍스트가 아닌 자료형'은 일반적인 입출력 방법(Write,read)으로는 데이터를 저장하거나 불러올 수 없음.

3, How?
(1) import pickle
(2) 파일명.pickle   # 확장자가 pickle
(3) 파일 쓰기 방식 pickle.dump(파일명,저장할 내용) 
(4) 파일 읽기 방식 pickle.load(파일명) 

※ pickle 파일은 binary 형태로 읽고 써야한다. 'wb' 'rb'

'''

import pickle 

# profile 파일을 생성하고 파일을 쓰기(dump)  

with open("profile.pickle",'wb') as profile_file:
    profile = {"이름":"박명수", "나이":30 , "취미":["축구","농구","골프"]}  # txt가 아닌 자료형 
    print(profile)
    pickle.dump(profile,profile_file)  #profile_file 파일에 profile의 값을 쓰기(dump)



# profile 파일을 읽기(load)

with open("profile.pickle",'rb') as profile_file:
    print(pickle.load(profile_file))



