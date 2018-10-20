#Name: Berkay baltas
#Date: 10/18/18
#This program creates a turtle

import turtle
comm = input("Enter directions: ")
bturt = turtle.Turtle()



for i in comm:
   if i == "F":
      bturt.forward(50)
   elif i =="L":
      bturt.left(90)
   elif i == "R":
      bturt.right(90)
   elif i == "^":
      bturt.penup()
   elif i == "v":
      bturt.pendown()
   elif i == "B":
      bturt.backward(50)
   elif i == "S":
      bturt.stamp()
   elif i == "l":
      bturt.left(45)
   elif i == "r":
      bturt.right(45)
   elif i == "p":
      bturt.color("purple")
