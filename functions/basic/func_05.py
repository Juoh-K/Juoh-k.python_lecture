## return 이용하여 비동기화 처리 연습

## 함수선언
def func1() :
    result = 100
    return result

def func2(x) :
    # print("반환값이 없는 함수 실행")
    print(f'func2()의 반환값 ==> {x}')

## 전역변수선언
hap = 0

## 메인코드
hap = func1()
print(f'func1()의 반환값 ==> {hap}')
func2(hap)