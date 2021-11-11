from myTurtle import *
import turtle

# 전역변수선언
inStr = ''
swidth, sheight = 300, 300
tX, tY, t_angle, t_size = [0] * 4

# 메인코드
turtle.title('거북이 글자쓰기(모듈버전)')
turtle.shape('turtle')
turtle.setup(width = swidth +50, height = sheight + 50 )
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.speed(10)

inStr = getString()

for ch in inStr :
    
    tX, tY, t_angle, t_size = getXYAS(swidth, sheight)
    r, g, b = getRGB()

    turtle.goto(tX, tY)
    turtle.left(t_angle)

    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은고딕', t_size, 'bold'))

turtle.done()