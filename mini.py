import turtle

turtle.bgcolor("black")
t=turtle.Turtle()
t.speed(0)
t.width(1)
t.hideturtle()

n=300
l=100
a=91

for i in range(n):
    color=["red","green","blue","yellow","purple","orange","pink","brown","gray","black"]
    t.color(color[i%10])
    t.forward(l)
    t.left(a)
    l+=1

turtle.done()
