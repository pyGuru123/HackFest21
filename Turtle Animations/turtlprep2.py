from turtle import *

colors = ['yellow', 'orange', 'red', 'green', 'blue', 'purple']
bgcolor('black')

for i in range(120):
	pencolor(colors[i%6])
	pensize(15)
	speed(20)
	circle(i)
	forward(i)
	right(59)
	forward(i)

exitonclick()

