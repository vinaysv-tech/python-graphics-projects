from turtle import *
import colorsys as cs
bgcolor('black')
speed(0)
pensize(3)
h=0
up()
goto(80, 90)
down()
for i in range(180):
    c=cs.hsv_to_rgb(h,1,1)
    h+=0.007
    pencolor(c)
    begin_fill()
    lt(105)
    fd(210-i)
    circle(-40, -150)
    fd(210-i)
    circle(-30, -150)
    end_fill()
done()