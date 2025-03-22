# Joshua Lamb
# 3-22-2025
# P4LAB1A
# Use turtle and loops to draw a square and triangle



#Import the library
import turtle

#Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

#Set turtle options
pen.pensize(5)
pen.pencolor("purple")
pen.shape("arrow")

#For loop to draw square
for side in range(4):
    pen.forward(200)
    pen.left(90)

#Reorient turtle to draw triangle
pen.right(105)

#While loop to draw triangle
sides = 3
while sides > 0:
    pen.forward(200)
    pen.right(120)
    sides = sides - 1
    
#Wait for user to close window
win.mainloop()
