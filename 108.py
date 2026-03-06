from turtle import *
from colorsys import *
bgcolor('black')
width(8)
tracer(50)
h = 0
for i in range(500):
    c = hsv_to_rgb(h,1,1)
    h += 0.05
    color(c)
    fillcolor('black')
    begin_fill()
    circle(i/4, 60)
    rt(20)
    up()
    goto(0,0)
    down()
    circle(i/4, 30)
    rt(55)
    fd(i/6)
    end_fill()
done()
