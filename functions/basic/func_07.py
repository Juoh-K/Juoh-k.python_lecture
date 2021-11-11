## keyword parameter

# 키워드 인자는 항상 위치 인자보다 뒤에 있어야 함
# 키위드 인자와 위치인자가 같이 있을경우 순서는 항상 준수
# 단, 키워드 인자만 있을 경우 호출시 순서는 상관 없음

def para_func(v1, v2, v3 = 0, v4 = 0) :
    result = 0
    result = v1 + v2 + v3 + v4
    return result

hap = 0

hap = para_func(10,20)
print(f'매개변수가 2개인 함수를 호출한 결과 : {hap}')
hap = para_func(10,20,30,40)   
print(f'매개변수가 4개인 함수를 호출한 결과 : {hap}')

hap1 = para_func(10,20,v4=30, v3=40)
print(f'매개변수가 4개인 함수를 호출한 결과 : {hap}')

