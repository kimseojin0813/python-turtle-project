import turtle as t
import time

t.bgcolor('pink')
t.hideturtle()
t.up()

for i in range(10, 0, -1):
    t.write(str(i), False, 'center', ('', 30))
    time.sleep(1)
    t.clear()

t.mainloop()