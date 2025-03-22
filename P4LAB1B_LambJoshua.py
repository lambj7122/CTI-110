# Joshua Lamb
# 3-22-2025
# P4LAB1B
# Use turtle to draw initials



#Import the library
import turtle

#Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

#Set turtle options
pen.pensize(5)
pen.pencolor("purple")
pen.shape("arrow")

#Draw a capital J
pen.right(90)
pen.forward(180)
for turn in range(18):
    pen.right(10)
    pen.forward(10)

#Move pen for next letter
pen.penup()
pen.forward(170)
pen.right(90)
pen.forward(180)
pen.pendown()

#Draw a capital L
pen.right(90)
pen.forward(230)
pen.left(90)
pen.forward(120)
    
#Wait for user to close window
win.mainloop()
