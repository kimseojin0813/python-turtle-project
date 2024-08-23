import turtle as t

def petale():
        # 꽃잎 하나
        for i in  range(2):
            t.circle(150, 110) # 두번째 매개변수는 각도를 의미한다.
            t.left(70)

def draw_flower():
    t.color('pink')
    t.begin_fill()
    # 꽃그리기
    for j in range(5):
        petale()
        t.left(360/5)
    t.end_fill()

    t. goto(3, -30)
    t.color('hotpink')
    t.begin_fill()
    t.circle(30)
    t.end_fill()


t.speed(0)


t.hideturtle()
t.bgcolor('ivory')

draw_flower()

t.mainloop()