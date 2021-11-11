## 지역변수, 전역변수

def func1() :
    a = 10
    print(f'func1()에서 a값 : {a}')

def func2() :
    print(f'func2()에서 a값 : {a}')

## 전역변수선언
a = 20

## 메인코드
func1()
func2()