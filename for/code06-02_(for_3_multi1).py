## for문 이용하여 구구단 만들기

dan = 0

dan = int(input("단을 입력하세요 : "))

for i in range(1,10,1) :
    print(f'{dan} X {i} = {dan*i}')
    # print("%d x %d = %2d" % (dan, i, dan*i))