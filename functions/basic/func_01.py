## function basic


## 함수선언
def plus(v1, v2) :

    result = 0
    result = v1 + v2
    return result

## 전역변수선언
hap = 0

## 메인코드
vv1 = 100
vv2 = 200

hap = plus(vv1, vv2)
print(f'{vv1}과 {vv2}의 plus() 함수결과는 : {hap}')