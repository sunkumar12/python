import turtle as n
import random
n.colormode(255)
n.speed(10)
n.pensize(4)
for i in range(12):
    n.color('green')
    n.forward(100)
    n.left(60)
    n.forward(20)
    n.left(60)
    n.forward(50)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    n.color(r,g,b)
    for i in range(10):
        n.forward(30)
	n.left(160)
    n.right(30)
    n.penup()
    n.setposition(0, 0)
    n.pendown()
    n.right(10)
turtle.done()
sanjeet