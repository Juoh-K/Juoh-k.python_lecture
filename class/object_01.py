## class / property / method

# 새로운 객체 생성
class Car :

    # property 생성
    color = ""
    speed = 0

    # method 생성
    def up_spped(self, value) : 
        # self : 생성하는 객체 자신의 properties 를 이용
        # 함수가 동작하는 최소 시작점(시작주소)를 의미 ?? 
        self.speed += value

    def down_speed(self, value) :
        self.speed -= value

car = Car()  # car 라는 새로운 인스턴스 만듦
print(car.speed) # 그 새로운 인스턴스(객체)는 . 를 이용할 수 있다
car.up_spped(500)
print(car.speed)

