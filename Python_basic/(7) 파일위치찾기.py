# 파일의 위치(디렉토리)확인

import inspect
import random
print(inspect.getfile(random))  #'random' 이라는 모듈(파일)이 어느 위치에 있는지 알려주는 함수 inspect()