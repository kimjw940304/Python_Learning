'''
(1) 모듈 : 함수나 클래스등을 담고 있는 파일  (확장자 = .py)

cf) 모듈을 import하려면 모듈을 사용하려는 파일과 모듈 파일이 같은 경로에 있거나 Python lib폴더에 있어야 사용가능
cf) class나 함수명 '만을' 다른파일에서 import를 할 수 없다.  
    ex. Import 함수명  (에러발생)
        Import class명 (에러발생)
    단, from 모듈명 import 함수명 (에러발생X)
        from 모듈명 Import class명 (에러발생X)
    즉, 파이썬 파일에서 다른 파일의 함수or 클래스를 가져와 쓰려면 반드시 처음에는 '모듈명'이 불러와져야한다. 
                     (단, 패키지가 더 상위개념 )

    # 패키지 > 모듈 > 클래스 ,함수 ,변수... #
'''

import theater_module as mv # theater_module을 임포트 하는데 줄여서 mv라고 하겠다 라는뜻. 
mv.price(3) # mv 모듈의 price함수를 호출


from theater_module import * # theater_module의 모든 함수를 사용하겠다는 의미.
price(3) #theater_module 의 price() 함수를 간단하게 호출가능

'''
(2) Package :모듈들을 모아놓은 집합

How?
(1) Package명을 갖는 New Folder를 만든다. (이게 패키지의 디렉토리값)
(2) 그 폴더안에 모듈.py 들을 만들어 넣어두면된다. 
(3) 그 폴더안에 __init__.py 파일을 만든다
(4) __init__.py 를 작성    
__all__["모듈1이름","모듈2이름"...]  <--이렇게 정의를 해줘야 * 해도 불러올 수 있음


cf) (4)을 작성하지 않을경우
from 패키지명 import * <-- 패키지의 모든 모듈을 사용하겠다고 정의를해도 오류가 발생
        
''' 