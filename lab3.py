from graphics import *
import turtle


#Task2:
#(a) Evaluati scriptul;
#(b) Completati la 8 culori pentru generare; schimbati culoare background si viteza de generare.
#(c) Realizati un program care sa se genereze dupa un patrat ?

t = turtle.Turtle()
#turtle.bgcolor("grey")
turtle.bgcolor("light pink")
turtle.pensize(3)
#turtle.speed(1)
turtle.speed(100)
while (True):
 for i in range(4):
    for colors in ["red", "blue", "magenta", "green", "pink","yellow", "white","black"]:
        turtle.color(colors)
        turtle.circle(50)
        turtle.left(20)
    turtle.hideturtle()
turtle.mainloop() 

