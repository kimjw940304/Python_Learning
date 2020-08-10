# PIL : Python Image Liabrary(설치 필요 by. pip install Pillow)
import time
from PIL import ImageGrab

# 프로그랭 작동시 세팅 시간 간격으로 이미지를 캡쳐&저장 기능
time.sleep(5) # 5초 대기 : 사용자가 준비하는 시간

for i in range(1,11): # 2초 간격으로 10개 이미지를 저장
    img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴
    img.save("image{}.png".format(i)) # 파일로 저장
    time.sleep(2)
