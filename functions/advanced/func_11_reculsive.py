# 입력한 숫자를 1까지 세는 함수를 재귀 함수 사용
def count(num) :
    if num >= 1 :
        print(num, end ='')
        count(num -1)
    else :
        return

count(10)
count(20)

