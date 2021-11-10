# SyntaxError: cannot assign to literal
# 10 = 100

# TypeError: can only concatenate str (not "int") to str
# sel = input("진수 타입을 넣으시오(16/10/8/2)")
# print(sel + 16)
# print(int(sel) + 16)
# print(type(sel))
# print(float(sel) + 16)
# print(type(sel))

# !!! 정말 중요 !!!
# 파이썬에서 블럭을 지정할 때는 => indent(들여쓰기)를 맞춘다
# IndentationError: unexpected indent
# sel = int(input("진수 타입을 넣으시오(16/10/8/2)"))
#  num = input('값 입력:') # 위와 같은 라인 아닌경우 자동에러탐지

# SyntaxError: invalid syntax
# print(""나는"사람이다.")
# solve-1 : ', " 같이 사용 하지 않는다
# print('"나는"사람이다.') 
# solve-2 : ''' ~~~ ''' 사용
# print('''
# "나는"사람이다.''')