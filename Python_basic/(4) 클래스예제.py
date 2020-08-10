# Class 예제 
'''
(출력 예제)

총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

[코드]
'''

class House:
    #  매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.competion_year =completion_year

    
    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.competion_year)


houses = []  # 총 매물 리스트 생성
house1 = House('강남','아파트','매매','10억','2010년')
house2 = House('마포','오피스텔','전세','5억','2007년')
house3 = House('송파','빌라','월세','500/50','2000년')

houses.append(house1)
houses.append(house2)
houses.append(house3)
'''
for i in range(1,4):
    house_m = "house"+str(i)
    houses.append(house_m)
'''
print("총 {0}대의 매물이 있습니다".format(len(houses)))

for house in houses:
    House.show_detail(house)


 