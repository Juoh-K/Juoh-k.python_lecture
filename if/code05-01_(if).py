# !! 주의 !! 
# input 값은 문자형으로 default 입력 됨

# a = int(input("비교할 숫자(정수)를 입력하시오 :")) 
a = float(input("비교할 숫자(실수)를 입력하시오 :"))

if a < 100 :
    print(f'{a}(은)는 100보다 작군요')
elif a > 100 :
    print(f'{a}(은)는 100보다 작지 않군요')
else :
    print(f'{a}(은)는 100과 같군요')
