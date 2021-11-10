# for 문 및 문자열 갯수 && continue 사용법

a = ["a", "b", "c"]
b = "Hello World"

print(len(b))

# 대문자를 제외한 문자 출력
# for i in b :
#     if i  != "H" and i != "W" :
#         print(i)

for i in b :
    if i == "H" or i == "W" :
        continue
    print(i)