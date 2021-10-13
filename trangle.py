from turtle import *
import random

nums = ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')

color("#AFD7AF")


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
color("#0F0F0F")

goto(105, 65)


for i in range(1, 8):
    penup()

    circle(10, 80)
    seth(i*20)
    posi = pos()

    colstr = '#'
    for j in range(0, 3):
        colstr += (str(hex(i*2))[2:] + random.choice(nums))
    color(colstr)
    begin_fill()
    left(65-(i*5))
    forward(80 + (i*10))
    left(60)
    forward(85 + (i*8))
    goto(posi)
    end_fill()

hideturtle()
done()
