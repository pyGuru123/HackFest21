import turtle

screen = turtle.Screen()
turtle.speed(50)



for i in range(80):
	turtle.circle(25*i)
	turtle.forward(5)
	turtle.left(5)
	turtle.circle(25*i)
	turtle.down()
	
turtle.exitonclick()

