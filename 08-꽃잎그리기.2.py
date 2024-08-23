import turtle as t
import random

def petal(size, angle):
        # 꽃잎 하나
        for i in  range(2):
            t.circle(size, angle) # 두번째 매개변수는 각도를 의미한다.
            t.left(180 - angle)

def draw_flower(petal_num, size, angle):
    t.color('pink')
    t.begin_fill()
    # 꽃그리기
    for j in range(petal_num):
        petal(size, angle)
        t.left(360/petal_num)
    t.end_fill()

    t. goto(3, -30)
    t.color('hotpink')
    t.begin_fill()
    t.circle(30)
    t.end_fill()


t.speed(0)


t.hideturtle()
t.bgcolor('ivory')

petal_num = random.randint(4, 10) 
petal_size = random.randint(50, 120)
petal_angle = random.randint(90, 130)

draw_flower(petal_num, petal_size, petal_angle)

t.mainloop()