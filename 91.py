from turtle import *
from colorsys import *
bgcolor("black")
tracer(0)
h = 0
for i in range(650):
    c = hsv_to_rgb(h,1,1)
    h = (h+0.5)%1
    up()
    goto(0,0)
    down()
    bgcolor("black")
    fillcolor(c)
    begin_fill()
    right(508)
    circle(i*0.5,24)
    fd(50)
    left(29)
    for k in range(11):
        fd(1)
        circle(k*0.5,299,steps=2)
    for j in range(3):
        fillcolor(c)
        begin_fill()
        circle((i*0.3)*(1-j *0.1),24)
        end_fill()
        right(120)
    end_fill()
    update()
done()