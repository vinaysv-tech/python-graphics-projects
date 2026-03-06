from turtle import *
tracer(30)
setposition(-40,-30)
bgcolor("black")
color('aqua')
for i in range(100):
    rt(i)
    circle(150, i)
    fd(70)
    right(270)
    fd(i)
    lt(1)
    hideturtle()
done()
