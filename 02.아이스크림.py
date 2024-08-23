import turtle as t

t.bgcolor('pink')



t.color('red')

t.begin_fill()
for i in range(3):
    t.forward(200)
    t.right(360/3)



t.end_fill()

t.forward(100)

t.color('lightgreen')

t.begin_fill()


t.circle(100)

t.end_fill()

t.goto(130, 100)

t.color('chocolate')

t.begin_fill()


t.circle(70)

t.end_fill()

t.color('gold')
t.begin_fill()

for i in range(5):
    t.forward(30)
    t.right(144)
t.end_fill()




t.mainloop()