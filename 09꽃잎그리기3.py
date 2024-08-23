import turtle as t
import random

def radom_color():
     r = random.randint(0, 255)
     g = random.randint(0, 255)
     b = random.randint(0, 255)
     return r, g, b

def petal(size, angle):
        # 꽃잎 하나
        for i in  range(2):
            t.circle(size, angle) # 두번째 매개변수는 각도를 의미한다.
            t.left(180 - angle)

def draw_flower(petal_num, size, angle):
    t.up()
    x_pos = random.randint(-300, 300)
    y_pos = random.randint(-300, 300)
    t.goto(x_pos, y_pos)
    t.color(radom_color())
    t.begin_fill()
    # 꽃그리기
    for j in range(petal_num):
        petal(size, angle)
        t.left(360/petal_num)
    t.end_fill()

    t. goto(x_pos +3,y_pos  -30)
    t.color(radom_color())
    t.begin_fill()
    t.circle(30)
    t.end_fill()


t.speed(0)
t.colormode(255)


t.hideturtle()
t.bgcolor('ivory')

for f in range(5):
     

    petal_num = random.randint(4, 10) 
    petal_size = random.randint(50, 120)
    petal_angle = random.randint(90, 130)

    draw_flower(petal_num, petal_size, petal_angle)

t.mainloop()