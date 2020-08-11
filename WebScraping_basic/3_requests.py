import requests

# (1) 웹 페이지에 접속시도시 오류 여부 확인 방법  (문제없는지? 권한이 있는지? 등등)

res = requests.get("http://naver.com")
print("응답코드:", res.status_code)         # 200 : 정상.

res2 = requests.get("http://nadocoding.tistory.com")
print("응답코드:", res2.status_code)        # 403 : 접근 권한 없음

    # (1-1) 접속 오류 알림 방식 1    _  . status_code
if res2.status_code == requests.codes.ok:   # requests.code.ok = 200 과 동일하다.
    print("정상입니다.")
else:
    print("문제가 생겼습니다.[에러코드",res2.status_code,"]")

    # (1-1) 접속 오류 알림 방식 2    _  .raise_for_status()
res.raise_for_status()                    # 오류가 발생하면(200이 아니면) 오류 띄우고 프로그램 즉시 종료.
print("웹 스크래핑을 진행합니다.")