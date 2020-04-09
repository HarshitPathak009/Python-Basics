import turtle
wn=turtle.Screen() #creates a graphics window
wn.bgcolor("green")
jamal=turtle.Turtle() #creates a turtle names ees
jamal.color("white")
jamal.pensize(5)
for i in range(0,180):
	jamal.forward(1)
	jamal.left(1)

wn.exitonclick() #exits the window on clicking the cross button