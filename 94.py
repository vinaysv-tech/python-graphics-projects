from turtle import *
from colorsys import *
bgcolor("black")
tracer(200)
pensize(2)
h = 0.001
for i in range(360):
    c=hsv_to_rgb(h,1,1)
    h+=0.0031
    color(c)
    up()
    goto(-8,0)
    down()
    fd(i/2)
    rt(859)
    fillcolor('black')
    begin_fill()
    circle(15,320)
    end_fill()
    bk(i/4)
    fd(i)
    rt(30)
done()
