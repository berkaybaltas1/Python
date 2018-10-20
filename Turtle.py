#Name: Berkay Baltas
#Date: August 30, 2018
#This program creates: An octagon.

#draws a square, using the turtle module
import turtle

#create a turtle
thomasH = turtle.Turtle()


for i in range(8):
    thomasH.forward(100) #Move forwad 100 steps
    thomasH.left(360/8) #turn 90 degrees to the left
