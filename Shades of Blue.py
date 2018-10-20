#Name: Berkay Baltas
#Date: 09/13/2018
#This program creates a shade of blue

import turtle

turtle.colormode(255)
tess = turtle.Turtle()

tess.backward(100)
for i in range(0,255,10):
    tess.forward(10)
    tess.pensize(i)
    print(i)
    tess.color(0,0,i)
    
    
    

