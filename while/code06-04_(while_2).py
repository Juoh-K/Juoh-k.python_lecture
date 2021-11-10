## while 반복문 및 탈출구문(break)

ch = ""
a, b = 0, 0

while True : 
    a = int(input("계산할 첫 번째 수를 입력하세요 : "))
    b = int(input("계산할 두 번째 수를 입력하세요 : "))
    ch = input("계산할 연산자를 입력하세요 : ")

    if ch == "+" :
        print(f'{a} + {b} = {a+b}')
    elif ch == "-" :
        print(f'{a} - {b} = {a-b}')
    elif ch == "*" :
        print(f'{a} * {b} = {a*b}')
    elif ch == "/" :
        print(f'{a} / {b} = {a/b}')
    elif ch == "%" :
        print(f'{a} % {b} = {a%b}')
    elif ch == "//" :
        print(f'{a} // {b} = {a//b}')
    elif ch == "**" :
        print(f'{a} ** {b} = {a**b}')
    else :
        print("연산자를 잘못 입력했습니다.")
    d = input("종료하시려면 'q'를 입력해주세요. 계속 하시려면 아무키나 눌러주세요!")
    if d == "q" :
        break
    
