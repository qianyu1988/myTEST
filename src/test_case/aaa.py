from turtle import *
from random import *
import time

def curvemove():
    time.sleep (0.000005)
    speed (10)
    hideturtle ( )
    for i in range (80):
        right (1)
        forward (1)
        print(i)
pensize(2)                  #调整画笔粗细
speed(1)                   #调节画笔速度
color ("red","red")  # 画笔颜色及填充颜色
begin_fill()                #开始填充
left(140)
fd(111.65)
curvemove()                 #调用函数
left(120)
curvemove()                 #调用函数
fd(111.65)
end_fill()                  #结束填充
hideturtle()                #隐藏画笔
done()

    # pensize (randint (3, 5))
    # x = (randint (-380, 384))
    # y = (randint (1, 270))
    # pencolor ("gold")
    # penup ( )
    # goto (x, y)
    # pendown ( )
# for j in range (5):
#     forward (20)
#     right (144)

# 画布大小
setup (800, 600, 200, 200)
hideturtle ( )
bgcolor ("dark slate blue")
curvemove ( )

