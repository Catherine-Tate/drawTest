from turtle import *

color("#080808")



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

begin_fill()
goto(65, 85)
pendown()
left(85)
forward(87)
left(60)
forward(85)
goto(65, 85)
end_fill()



for i in range(1, 8):
    penup()

    circle(10, 80)
    seth(i*20)
    posi = pos()

    colstr = '#' + (str(hex(i*2))[2:] + 'a')*3
    color(colstr)
    begin_fill()
    left(65-(i*5))
    forward(80 + (i*10))
    left(60)
    forward(85 + (i*8))
    goto(posi)
    end_fill()


done()
