'''
 # 예외처리 
 
(1) 예외발생시 except의 실행코드2를 실행.

try:
    실행코드1 ~
except:
    실행코드2 ~

(2) 예외발생시 except의 실행코드2를 실행.예외 발생X 경우 실행코드1이 끝나면 실행코드3을 실행.

try:
    실행코드1 ~
except:
    실행코드2 ~
else:
    실행코드3~

(3) 예외발생시 except의 실행코드2를 실행 & 오류 유무와 무관하게 마지막에 실행코드3을 실행

try:
    실행코드1 ~
except:
    실행코드2 ~
finally:
    실행코드3 ~

(4) 코드에서 예외 발생 내용을 확인

try:
    실행코드1!
except:
    실행코드2~
except Exception as e:  # 오류 코드를 e 라는 변수에 저장
    print(e)            # 오류 코드 출력

(5) 코드에서 예외 발생 내용시 특정 오류일때만 오류코드를 확인

try:
    실행코드1!
except:
    실행코드2~
except ValueError as err:                    # ValueError가 발생했을때는
    print("에러! 잘못된 값을 입력했습니다")     # 해당 오류 코드를 출력해준다.

'''

# 의도적으로 에러코드 발생  raise
try:
    print("한 자리 숫자 나누기 전용 계산기 입니다")
    num1 = int(input("첫 번째 숫자를 입력하시오:"))
    num2 = int(input("두 번째 숫자를 입력하시오:"))
    if num1 >= 10 or num2 >=20:
        raise ValueError           # if문에 해당할 경우 의도적으로 에러를 발생(raise)
    print('{0}/{1}={2}입니다.'.format(num1,num2,int(num1/num2)))

except ValueError:
    print("잘못된 값을 입력하셨습니다 한 자리 숫자만 입력하세요")

# 사용자 정의 에러 class 클래스명(Exception)

class BigNumberError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기 입니다")
    num1 = int(input("첫 번째 숫자를 입력하시오:"))
    num2 = int(input("두 번째 숫자를 입력하시오:"))
    if num1 >= 10 or num2 >=10:
        raise BigNumberError("입력값: {0} , {1}".format(num1,num2))           # 10보다 큰값 입력시 사용자가 정의한 클래스를 호출
    print('{0}/{1}={2}입니다.'.format(num1,num2,int(num1/num2)))
except BigNumberError as err:
    print(err)