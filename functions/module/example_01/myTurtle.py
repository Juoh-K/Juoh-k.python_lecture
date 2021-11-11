import random
from tkinter.simpledialog import *
from tkinter import Tk

root = Tk()
root.withdraw()

def getString() :
    resStr = ''
    resStr = askstring('문자열 입력', '거북이 쓸 문자열 입력')
    print(resStr)
    return resStr
# getString()

def getRGB() :
    r, g, b = 0, 0, 0
    r = random.random()
    g = random.random() 
    b = random.random()
    return(r, g, b)
    # print(r, g, b)
# getRGB()

def getXYAS(sw, sh) :
    x, y, angle, size = 0, 0, 0, 0
    x = random.randrange(-sw / 2, sw / 2)
    y = random.randrange(-sw / 2, sw / 2)
    angle = random.randrange(0, 360)
    size = random.randrange(10, 50)
    return [x, y, angle, size]
    # print(x, y, angle, size)
# getXYAS(100,200)

