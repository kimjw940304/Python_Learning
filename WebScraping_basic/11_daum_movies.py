# 예제) DAUM 영화순위에서 "역대 관객순위" 상위5개씩 이미지를 저장하는 프로그램

import requests
from bs4 import BeautifulSoup


# (1) 2015년 ~ 2019년에 대한 역대 관객순위 URL 조회
for year in range(2015,2020): 
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')
      
    images = soup.find_all("img", attrs = {"class":"thumb_img"})

# (2) 이미지 파일 가져오기.
    for idx, image in enumerate(images):
            # url이 //로 시작할 경우 앞에 https: 를 추가해본다.  .startswith("??")
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:"+image_url
            print(image_url)

# (3) 가져온 이미지를 저장. (jpg파일로)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

            # img 파일은 txt가 아니가에 binary로 저장 "wb"
        with open("movie_{}_{}.jpg".format(year,idx+1),"wb") as f:
            f.write(image_res.content)      # 파일의 정보를 바로 content로 쓰는 방법 !!!

# (4) 페이지내 모든 이미지말고 ! 상위 5개만 다운로드
        if idx >= 4:
            break

