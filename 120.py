from turtle import *
from colorsys import *
tracer(2)
bgcolor("black")
h = 0
for i in range(5):
    color(hsv_to_rgb(h, 1, 1))
    for j in range(180):
        h += 0.0025
        fd(260)
        bk(260)
        rt(2)
        hideturtle()
done()