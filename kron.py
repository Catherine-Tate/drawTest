from turtle import *
import random

color("black")

#canvas
penup()
begin_fill()
goto(-300, 300)
forward(600)
seth(270)
forward(600)
seth(180)
forward(600)
seth(90)
forward(600)
end_fill()

penup()


color("white")
for i in range(1, 25):
	p1 = random.randint(-300, 300)
	p2 = random.randint(-300, 300)
	l1 = (8*i)%p1
	l2 = (6*l1)%p2
	l3 = (2*l2)%p1

	penup()
	goto(p1, p2)
	pendown()
	
	begin_fill()

	if(i%2 == 0):
		forward(l1)
		left(l2)
		forward(l3)
		right(l2)
		forward(l3)
	else:
		forward(l2)
		right(l2)
		forward(l1)
		left(l1)
		forward(l3)
	end_fill()



hideturtle()
done()