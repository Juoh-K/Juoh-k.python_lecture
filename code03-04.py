sel = int(input("진수 타입을 넣으시오(16/10/8/2)"))
num = input('값 입력:')

# 파이썬에서 블럭을 지정할 때는 => indent(들여쓰기)를 맞춘다
# (참고, \ (역슬래시) = 코딩이 길어져 다음줄로 이동시 \
# 밑의 줄도 같은 줄로 인식)
# tap key 1칸은 띄어쓰기(spacebar) 4칸과 같다
if sel == 16:
    num10 = int(num, 16)
    print(hex(num10)) #hex() : 16진수 표현 (0x100)
    print(bin(num10)) #bin() : 2진수 표현 방법 (0b100000000)

if sel == 2:
    num2 = int(num, 2)
    print(num2) # default 값 = 10진수
    print(bin(num2)) #bin() : 2진수 표현 방법 (0b100)
    print(hex(num2)) #hex() : 16진수 표현 (0x4)

