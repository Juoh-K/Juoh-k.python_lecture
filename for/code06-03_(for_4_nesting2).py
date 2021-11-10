## for문 중첩 이용하여 구구단 만들기

i = 0
j = 0

for i in range(2, 10, 1) :
    for j in range(1, 10, 1) :
        print(f'<{i}단>')
        print(f"{i} X {j} = {i*j}")
    print("") # 단수 별 띄워쓰기 용도 (별 의미 없음 ㅎㅎ)