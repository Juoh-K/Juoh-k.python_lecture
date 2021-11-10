
## practice
a = 5 ; b = 3
print(a+b , a-b, a*b, a/b, a//b, a%b, a**b)

a, b, c = 2, 3, 4
print(a + b - c, a + b * c, a * b / c)

a = 10
a += 5 ; print(a)
a -= 5 ; print(a)
a *= 5 ; print(a)
a /= 5 ; print(a)
a //= 5 ; print(a)
a %= 5 ; print(a)
a **= 5 ; print(a)

## Code04-01 : 연산자를 활용해서 동전 교환 프로그램 구현
# 변수 선언 부분 
money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

# 대입연산자 (자주 사용 ~ 중요함!!! )
# 메인 코드 부분
money = int(input("교환할 돈은 얼마?"))

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print("\n 500원짜리 ==> %d개" % c500) # d:정수, f:실수, s:문자
# print("100원짜리 ==> %d개" % c100)
print("100원짜리 ==> {}개" .format(c100)) # format 구문
# print("50원짜리 ==> %d개" % c500)
print(f"50원짜리 ==> {c50}개") # 리터럴 표현법 (f-string)
print("10원짜리 ==> %d개" % c10)
print("바꾸지 못한 잔돈 ==> %d원 \n" % money)

print(f'500원 짜리는 {c500}이고, 100원 짜리는 {c100}이고, \
50원 짜리는 {c50}이며, 10원 짜리는 {c10}이고, 잔돈은 {money}')

if(1234) : print("참이면 보여요") # '0'을 제외한 모든 수 = True
if(0) : print("거짓이면 안 보여요") # '0' = False
# if(not(0)) : print("거짓이면 안 보여요") # not(0) = True

print(0^1) # ^ : 같으면 0, 다르면 1
print(True^False) # 둘이 다르므로 1 = True 출력
print(int(True^False)) # 둘이 다르므로 1 = True 출력 => 숫자변환