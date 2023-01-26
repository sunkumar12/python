import turtle
def draw():
	window = turtle.Screen()
	window.bgcolor("white")

	nate = turtle.Turtle()
	nate.shape("turtle")
	nate.color("Blue")

	for x in range(30):
		for i in range(6):
			nate.forward(50)
			nate.right(50)
		nate.right(110)

	window.exitonclick()


draw()