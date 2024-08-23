import turtle as t
import time
import random

t.bgcolor('pink')
t.hideturtle()
t.up()

num_times = int(t.textinput('숫자기억 게임', '몇게의 숫자를 기억할까요?'))
t.write('숫자 기억하기 게임을 시작합니다', False, 'center', ('', 30))
time.sleep(3)
t.clear()

num = ''

for i in range(num_times):
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    rand_num = random.randint(1, 30)
    t.write(rand_num, False, 'center', ('', 70))
    num += str(rand_num) + ' '
    time.sleep(0.5)
    t.clear()

user_input = t.textinput('숫자 기억게임', '기얷한 숫자를 입력하세요.(공백)')

if user_input.strip() == num.strip():
    t.write('정답입니다.', False, 'center', ('', 30))
else:
    t.write('오답입니다.', False, 'center', ('', 30))
    t.goto(0,-50)
    t.write(f'정답은 {num}입니다', False, 'center', ('', 30))
    t.goto(0,-100)
    t.write(f'입력하신 숫자는{user_input}입니다', False, 'center', ('', 30))




t.mainloop()