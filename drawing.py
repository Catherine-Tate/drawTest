import turtle

from turtle import *


begin_fill()
color("#175676")
turtle.penup()
turtle.setpos(-450, 300)
turtle.seth(0)
turtle.forward(600)
turtle.seth(270)
turtle.forward(600)
turtle.seth(180)
turtle.forward(600)
turtle.seth(90)
turtle.forward(600)
end_fill()


color('#FAE1DF', '#D81159')


#circle
turtle.seth(0)
turtle.penup()
turtle.setpos(-50, -100)

turtle.pendown()
turtle.dot(90)

begin_fill()
turtle.penup()

#semi-triangle thing
tPos1 = (-70, 200)
turtle.setpos(tPos1)
turtle.seth(180)
turtle.left(20)
turtle.forward(155)
tPos2 = turtle.pos()
turtle.right(20)
turtle.forward(100)
tPos3 = turtle.pos()
end_fill()


turtle.penup()
newPos = (turtle.pos()[0]+50, turtle.pos()[1]-40)
turtle.seth(turtle.towards(-50, -100))
for i in range(0, 4):
    turtle.forward(70)
    if(i%2 == 0):
        turtle.dot(34)
#turtle.dot(22)
turtle.seth(75)
turtle.forward(200)
turtle.dot(60)

color('#880837')
begin_fill()
turtle.goto(tPos1)
turtle.pendown()
turtle.goto(tPos2)
turtle.goto(tPos3)
turtle.goto(tPos1)
end_fill()

hideturtle()
done()

