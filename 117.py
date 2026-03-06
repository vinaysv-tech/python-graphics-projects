from turtle import *
from colorsys import *
bgcolor('black')
speed(0)
h = 0
for _ in range(250):
    h +=0.009
    color(hsv_to_rgb(h,1,1))
    circle(130)
    right(5)
    hideturtle()
done()
