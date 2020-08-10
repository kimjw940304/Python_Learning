# 특정 키 값을 눌렀을때 스크린샷 및 저장
# keyboard 패키지 설치 필요 : pip install keyboard

import keyboard
from PIL import ImageGrab
import time

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))

# keyboard.add_hotkey("키값",동작함수)
keyboard.add_hotkey("F9",screenshot)
# 사용자가 esc를 누를 떄까지 프로그램 수행
keyboard.wait("esc")

