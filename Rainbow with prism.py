import turtle
import time
wn=turtle.Screen()
wn.setup(800,800)
wn.bgpic('raincolors.gif')
t=turtle.Turtle()

t1=turtle.Turtle('turtle')
t1.up()
t1.hideturtle()
t1.color('red')
t1.goto(0,-150)
t1.shapesize(4)
t1.showturtle()

clr=['red','orange','yellow','green',\
     'blue','indigo','violet']
t.color('white')
rainbow=[]
q=0
t.penup()
t.hideturtle()
t.goto(-275,-85)
t.setheading(29)
t.pensize(15)
t.pendown()
turtle.tracer(20)

for n in range (155):
    t.fd(1)
    X=t.xcor()
    Y=t.ycor()
    if X>-140:
        t.penup()
        X1=t.xcor()
        Y1=t.ycor()
for n in range (7):
        rainbow.append(turtle.Turtle())
        rainbow[n].hideturtle()
        rainbow[n].penup()
        rainbow[n].setposition(X1+5,Y1+3)
        rainbow[n].setheading(10-5*n)
        rainbow[n].pendown()
        rainbow[n].color(clr[n])
for m in range(70):
    for n in range (7):
        rainbow[n].pensize(5+0.35*m)
        if m>43+2*n:
            rainbow[n].setheading(-5*n)
        rainbow[n].fd(5)


