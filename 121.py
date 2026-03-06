from turtle import *
from colorsys import *
setposition(50,-50)
tracer(10)
bgcolor("black")
pensize(2)
h=0
for i in range(180):
    for i in range(4):
        h+= 0.003
        color(hsv_to_rgb(h,1,1))
        circle(70+i*5,90)
        fd(200)
        lt(90)
    rt(10)
done()
