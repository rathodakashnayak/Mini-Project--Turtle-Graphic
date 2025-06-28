# Mini-Project--Turtle-Graphic
==================
### Overview
This is a simple turtle graphic program that draws a square, a circle, and a triangle using the Turtle library in Python.
### Code

import turtle

turtle.bgcolor("black") # Set the background color to black
t=turtle.Turtle() # Create a turtle object
t.speed(0)
t.width(1) # Set the speed of the turtle to the fastest
t.hideturtle() # Hide the turtle cursor

n=300
l=100 # Initial length of the line
a=91  # Angle to turn the turtle

for i in range(n):
    color=["red","green","blue","yellow","purple","orange","pink","brown","gray","black"]
    t.color(color[i%10]) # Change color every iteration
    t.forward(l) # Move the turtle forward by l units 
    t.left(a)
    l+=1  # Increase the length of the line by 1 unit each iteration

turtle.done()

### Explanation
This code creates a turtle graphic that draws a square, a circle, and a triangle using a loop
The turtle starts at the origin (0,0) and moves forward by a certain length 
The turtle then turns left by a certain angle
The length of the line is increased by 1 unit each iteration, creating a spiral effect
The color of the turtle is changed every iteration, creating a colorful effect
### Output
The program will display a colorful spiral pattern on the screen.

============================================
