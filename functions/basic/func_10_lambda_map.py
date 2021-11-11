## lambda 와 map 함수 연습

list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
haplist = list(map(lambda n1, n2 : n1 + n2, list1, list2))
print(haplist)