## if_else

# a = int(input("비교할 숫자(정수)를 입력하시오 :"))
a = float(input("비교할 숫자(실수)를 입력하시오 :"))

b = 50
c = 100

if a > b :
    if a < c :
        print(f'{a}(은)는 {b}보다 크고 {c}보다 작군요')
    else :
        print(f'와~~ {a}(은)는 {c}보다 크거나 같군요')
else :
    print(f'에고~~ {a}(은)는 {b}보다 작거나 같군요')