from turtle import *
from colorsys import *
bgcolor("black")
tracer(20)
h = 0
for i in range(800):
    h+= 0.007
    color(hsv_to_rgb(h,1,1))
    goto(0, 0)
    fd(270)
    rt(2)
    circle(150,-90)
    end_fill()
    rt(90)
    hideturtle()
done()
