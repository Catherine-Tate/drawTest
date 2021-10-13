from turtle import *

color("#080808")


'''
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
'''
penup()
color("#0a0a0a")

begin_fill()
goto(65, 85)
pendown()
seth(0)
left(85)
forward(87)
left(60)
forward(85)
goto(65, 85)
end_fill()

for i in range(1, 5):
    penup()
    seth(180)
    forward(10)
    seth(270)
    forward(10)
    seth(0)
    posi = pos()

    colstr = '#' + (str(hex(i*2))[2:] + 'a')*3
    color(colstr)
    begin_fill()
    left(65+(30*i))
    forward(87)
    left(60)
    forward(85)
    goto(posi)
    end_fill()


done()
