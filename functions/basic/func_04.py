## 함수내에서 global 변수 선언

def func1() :
    global a
    a = 10
    print(f'func1()에서 a값 : {a}')

def func2() :
    print(f'func2()에서 a값 : {a}')

## 전역변수선언


## 메인코드
func1()
func2()