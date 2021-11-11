## 클래스 선언
class Car :
    name = ""
    color = ""
    speed = 0

    def __init__(self, name, speed, color) :
        self.name = name
        self.speed = speed
        self.color = color
    
    def get_name(self) :
        print("차량 이름 : ", self.name)
        return self.name

    def get_speed(self) :
        print("차량 속도 : ", self.speed)
        return self.speed

    def get_color(self) :
        print("차량 색상 : ", self.color)
        return self.color


## 변수 선언
car1, car2 = None, None

## 메인코드
car1 = Car("Audi", 0, "black")
car2 = Car("Benz" , 30, "white")

print(f'{car1.get_name()}의 현재 속도는 {car1.get_speed()}이고 색상은{car1.get_color()}입니다')
print(f'{car2.get_name()}의 현재 속도는 {car2.get_speed()}이고 색상은{car2.get_color()}입니다')
