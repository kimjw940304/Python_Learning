import requests
from bs4 import BeautifulSoup

# url의 값을 받아서 soup 객체로 만드는 함수 
def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    return soup

# 날씨 정보 생성 함수
def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EB%84%A4%EC%9D%B4%EB%B2%84%EB%82%A0%EC%94%A8&tqi=UzpXxlp0Jywssv9vssossssssBh-248435"
    soup = create_soup(url)

    # 기상 예측
    cast = soup.find("p", attrs= {"class":"cast_txt"}).get_text()
    # 기온 정보 
    curr_temp = soup.find("p", attrs = {"class":"info_temperature"}).get_text().replace("도씨", "")
    max_temp = soup.find("span", attrs ={"class":"min"}).get_text()
    min_temp = soup.find("span", attrs ={"class":"max"}).get_text()
    # 강수 확률
    morning_rain_rate = soup.find("span", attrs= {"class":"point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs= {"class":"point_time afternoon"}).get_text().strip()

    # 출력
    print(cast)
    print("현재 {} (최저 {} / 최고 {})".format(curr_temp,max_temp,min_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate,afternoon_rain_rate)) 

def scrape_headline_news():
    # 뉴스 url및 soup 객체 생성
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/"
    soup = create_soup(url)
                                                # find_all 에서 limit=3 즉 3개만 찾는다.
    news_list = soup.find("ul", attrs= {"class":"hdline_article_list"}).find_all("li",limit=3)
    # 순차적 출력
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print("{}. {}".format(index+1,title))
        print("  (링크 : {}".format(link))
    print()

 
if __name__ == "__main__":
    # scrape_weather()    # 오늘의 날씨 정보 호출
    scrape_headline_news()  # 헤드라인 뉴스 호출 