## 클래스 선언
class Car :
    color = ""
    speed = 0

    def up_spped(self, value) : 
        self.speed += value

    def down_speed(self, value) :
        self.speed -= value

## 메인코드
my_car1 = Car()
my_car1.color = "빨강"
my_car1.speed = 0

my_car2 = Car()
my_car2.color = "파랑"
my_car2.speed = 0

my_car3 = Car()
my_car3.color = "노랑"
my_car3.speed = 0

my_car1.up_spped(30)
print(f'자동차1의 색상은{my_car1.color}이며, 현재속도는 {my_car1.speed}km입니다.')
my_car2.up_spped(60)
print(f'자동차2의 색상은{my_car2.color}이며, 현재속도는 {my_car2.speed}km입니다.')
my_car3.up_spped(0)
print(f'자동차3의 색상은{my_car3.color}이며, 현재속도는 {my_car3.speed}km입니다.')