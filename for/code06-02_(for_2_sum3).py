## 홀수(odd) / 짝수(even) 합계 구하기

hap = 0

# method.1
# for i in range(501,1001,2) : # range 에서 간격2로 설정
#     hap += i

# method.2 
for i in range(501,1001,1) : # if 문으로 짝수 설정
    if i % 2 == 1 :
        hap += i

# # method.3 (continue 사용하여) (수정중...)
# for i in range()

# print("500과 1000사이에 있는 홀수의 합계 : %d" % hap)
print(f"500과 1000사이에 있는 홀수의 합계 : {hap}")

