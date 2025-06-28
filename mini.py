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
