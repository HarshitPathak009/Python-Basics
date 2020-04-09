import turtle as t
wn = t.getscreen()
wn.bgcolor("lightgreen")
ss=t.Turtle()
ss.color("Blue")
ss.shape("turtle")
ss.up()
for size in range(5,60,2):
  ss.stamp()
  ss.forward(size)
  ss.right(size)
wn.exitonclick()