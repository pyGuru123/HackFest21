import os
import turtle
import time
import random

delay = 0.1

#Score :
total = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#Snake Target

tar = turtle.Turtle()
tar.speed(0)
tar.shape("circle")
tar.color("black")
tar.penup()
tar.goto(0, 100)

segments = []

#Scoring :
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Score : 0  High Score : 0", align="center", font=("Courier", 24, "normal"))

#Fucntions for navigation :
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"

#Functions for moving:
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

#Main game loop
while True:
    wn.update()
    #Check if the snake hits the border :
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for i in segments:
            i.goto(1000, 1000)
        # Clear the segments list
        segments.clear()
        delay = 0.1
        total = 0
        score.clear()
        score.write("Score : {}  High Score : {}".format(total, high_score), align="center", font=("Courier", 24, "normal"))

    #Check if the snake reaches its target
    if head.distance(tar) < 20:
        #Move tar to a random coordinate
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        tar.goto(x, y)

        #Adding a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        total += 10
        high_score = max(high_score, total)
        score.clear()
        score.write("Score : {}  High Score : {}".format(total, high_score), align = "center", font=("Courier", 24, "normal"))

    # Moving the snake
    for i in range(len(segments) -1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)
    #Move the start of snake to where the head is
    if(len(segments) > 0):
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    #Check if the snake hits itself
    for i in segments:
        if i.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for i in segments:
                i.goto(1000, 1000)
            # Clear the segments list
            segments.clear()
            total = 0
            delay = 0.1
            score.clear()
            score.write("Score : {}  High Score : {}".format(total, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
