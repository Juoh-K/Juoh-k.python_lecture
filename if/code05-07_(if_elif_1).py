## 삼항 연산자 를 사용한 if문

# a = int(input("비교할 숫자(정수)를 입력하시오 :"))
a = float(input("비교할 숫자(실수)를 입력하시오 :"))

b = 60

# res = ''
# if a >= b :
#     res = '합격'
# else :
#     res = '불합격'   
# print(res)

res = '합격' if a >= b else '불합격'
print(res)