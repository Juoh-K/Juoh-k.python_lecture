## if_elif

# a = int(input("비교할 숫자(정수)를 입력하시오 :"))
a = float(input("비교할 숫자(실수)를 입력하시오 :"))

b = 90
c = 80
d = 70
e = 60

if a >= b :
    print(f'A 학점입니다.')
elif a >= c :
    print(f'B 학점입니다.')
elif a >= d :
    print(f'C 학점입니다.')
elif a >= e :
    print(f'D 학점입니다.')
else :
    print(f'F 학점입니다.')