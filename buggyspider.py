import turtle as trtl

painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)
leg=8
length = 150
legdis = 360 / (leg)
legdis2= 360 / (leg)
painter.pensize(5)
n = 0
while (n<4):
  painter.goto(0,20)
  painter.pendown()
  painter.setheading(legdis+25*n)
  painter.circle(length,45)
  painter.penup()
  n = n + 1
n=0
while (n<4):
  painter.goto(0,20)
  painter.pendown()
  painter.setheading(legdis2+25*n)
  painter.circle(length, -45)
  painter.penup()
  n= n+1
painter.penup()
painter.goto(-5,30)
painter.pendown()
painter.color("white")
painter.pensize(10)
painter.circle(5)
painter.penup()
painter.goto(-5,10)
painter.pendown()
painter.circle(5)


painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()