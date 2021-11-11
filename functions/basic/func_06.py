## func_multi_return

def multi_1(v1, v2):
    retList = []
    res1 = v1 + v2
    res2 = v1 - v2
    retList.append(res1)
    retList.append(res2)
    return retList

def multi_2(v1, v2):
    retList = []
    res1 = v1 + v2
    res2 = v1 - v2
    return res1, res2

myList = multi_1(100, 200)
sum, sub = myList[0], myList[1]
ret = multi_2(300, 400)

## 결과값이 튜플 형태로 나오는것 확인!! 중요!!
print(f"multi_1에서 반환한 값 ==> {sum}, {sub}")
print(f"multi_2에서 반환한 값 ==> {ret}")

# ## 전역변수선언
# my_list_1 = []
# my_list_2 = []
# hap1, sub1 = 0, 0
# hap2, sub2 = 0, 0

# ## 메인코드
# my_list_1 = multi_1(100,100)
# my_list_2 = multi_2(200,400)
# hap1 = my_list_1[0]
# sub1 = my_list_1[1]
# hap2 = my_list_2[0]
# sub2 = my_list_2[1]

# print(f'multi_1()의 반환값 ==> ({hap1},{sub1})')
# print(f'multi_2()의 반환값 ==> ({hap2},{sub2})')