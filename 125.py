from turtle import *
from colorsys import *
bgcolor("black")
tracer(20)
h = 0
b = "black"
for i in range(800):
    h+= 0.005
    color(hsv_to_rgb(h,1,1),b)
    goto(0, 0)
    begin_fill()
    fd(270)
    lt(90)
    circle(150,-90)
    end_fill()
    lt(2)
    hideturtle()
done()
