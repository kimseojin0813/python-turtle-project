import turtle as t
import random

def com_choice():
    random_choice = random.randint(0,2)
    com.shape(images[random_choice])
    return com_list[random_choice]

def result_print(user_c, com_c):
    global user_score, com_score
    t.clear()
    t.goto(0, -250)

    if user_c == com_c:
        t.write('무승부', False, 'center', ('',50))
    elif winning_case[user_c] == com_c:
        user_score += 1
        user_pen.clear()
        user_pen.write(user_score, False, 'center', ('',50))
        t.write('승', False, 'center', ('',50))
    else:
        com_score += 1
        com_pen.clear()
        com_pen.write(com_score, False, 'center', ('',50))
        t.write('패', False, 'center', ('',50))

def rock(x, y):
    user.shape(rock_gif)
    com = com_choice()
    result_print('rock', com)

def scissors(x, y):
    user.shape(scissors_gif)
    com = com_choice()
    result_print('scissors', com)

def paper(x, y):
    user.shape(paper_gif)
    com = com_choice()
    result_print('paper', com)

# 1. 기본 설정
t.bgcolor('lavender')
t.title('가위 바위 보')
t.hideturtle()
t.up()

# 이미지를 정의
rock_gif = './images/rock.gif'
scissors_gif = './images/scissors.gif'
paper_gif = './images/paper.gif'

# turtle의 shape을 추가...
t.addshape(rock_gif)
t.addshape(scissors_gif)
t.addshape(paper_gif)

images = [rock_gif, scissors_gif, paper_gif]
com_list = ['rock', 'scissors', 'paper']
winning_case = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

user_score = 0
com_score = 0

# 사용자의 turtle객체를 생성
user = t.Turtle()
user.up()
user.speed(0)
user.goto(-150, 200)
user.write('나의 선택', False, 'center', ('', 30))
user.goto(-150, -50)
user.shape(images[0])

# 컴퓨터의 turtle객체를 생성
com = t.Turtle()
com.up()
com.speed(0)
com.goto(150, 200)
com.write('컴퓨터의 선택', False, 'center', ('', 30))
com.goto(150, -50)
com.shape(images[0])

#  사용자의 점수를 쓰기위한 turtle객체를 생성
user_pen = t.Turtle()
user_pen.ht()
user_pen.up()
user_pen.goto(-150, 100)
user_pen.write( user_score, False, 'center', ('', 50))

#  컴퓨터의 점수를 쓰기위한 turtle객체를 생성
com_pen = t.Turtle()
com_pen.ht()
com_pen.up()
com_pen.goto(150, 100)
com_pen.write( user_score, False, 'center', ('', 50))


t.onscreenclick(rock, 1)
t.onscreenclick(scissors, 2)
t.onscreenclick(paper, 3)


t.mainloop()

# 연습입니다