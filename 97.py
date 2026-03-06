from turtle import *
from math import sin,cos
from colorsys import *

bgcolor("black")
hideturtle()
speed("fastest")
tracer(0)

def print(R,r,d,angle,theta):
	penup()
	goto(R-r+d,0)
	pendown()
	for i in range(0,3000):
		angle+=theta
		d+=0.1
		x=(R-r)*cos(angle)
		y=(R-r)*sin(angle)
		x=((R-r)*cos(angle)
		   +d*cos(((R-r)/R)*angle))
		y=((R-r)*sin(angle)
		   -d*sin(((R-r)/R)*angle))
		goto(x,y)
		
for j in range(300):
	reset()
	h=j/100
	cr=hsv_to_rgb(h,1,1)
	color(cr)
	pensize(2)
	print(110,120,-35,0,j/200)
	getscreen().update()
exitonclick()
