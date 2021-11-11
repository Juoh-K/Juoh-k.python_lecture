## 사칙연산 계산기

## 함수선언
def calc(v1, v2, op) :
    result = 0
    if op == '+' :
        result = v1 + v2
    elif op == '-' :
        result = v1 - v2
    elif op == '*' :
        result = v1 * v2
    elif op == '/' :
        result = v1 / v2
    
    return result

## 전역변수선언
res = 0
var1, var2, oper = 0, 0, ""

## 메인코드
oper = input("계산을 입력하세요(+, -, *, /) : ")
var1 = int(input("첫 번째 수를 입력하세요 : "))
var2 = int(input("두 번째 수를 입력하세요 : "))

res = calc(var1, var2, oper)

print(f'##사칙연산계산기 : {var1} {oper} {var2} = {res}')
