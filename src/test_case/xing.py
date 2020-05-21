import turtle
import random

t = turtle.Turtle()
t.speed(0)
# # 绘制黑夜
# t.width(80)
# for x in range(20):
#     t.up()
#     t.goto(-250, 250 - x * 60)
#     t.down()
#     t.color(x * 10, x * 10, x * 10)
#     t.fd(1000)
# t.pensize(1)
# 绘制出五角星
for k in range(30):
    t.color(255, 255, random.randint(0, 200))
    w = random.randint(4, 8)
    i = random.randint(-200, 200)
    j = random.randint(100, 300)
    t.up()
    t.goto(i, j)
    t.down()
    t.begin_fill()
    for y in range(5):
        t.fd(w)
        t.left(72)
        t.fd(w)
        t.right(144)
    t.end_fill()
# 四角星
'''for x in range(50):
    t.color(255,255,random.randint(0,200)) 
    w = random.randint(4,8)
    i=random.randint(-200,200)
    j=random.randint(100,300)
    t.up()
    t.goto(i,j)
    t.down()
    t.begin_fill()
    for x in range(8):
        if x>0 and x%2==0:
            t.right(120)
        else:
            t.left(30)
        t.forward(w)
    t.end_fill()
'''


