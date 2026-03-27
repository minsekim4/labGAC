from graphics import *
import turtle


#Task2:
#(a) Evaluati scriptul;
#(b) Completati la 8 culori pentru generare; schimbati culoare background si viteza de generare.
#(c) Realizati un program care sa se genereze dupa un patrat ?

c = turtle.Turtle()
t = turtle.Turtle()
#turtle.bgcolor("grey")
turtle.bgcolor("light pink")
c.pensize(3)
t.pensize(3)
#turtle.speed(1)
c.speed(100)
t.speed(100)
culori = ["red", "blue", "magenta", "green", "pink", "yellow", "white", "black"]
while (True):
   # for i in range(4):
   #     for colors in culori:
   #         c.color(colors)
   #         c.circle(50)
   #         c.left(20)
   #     c.hideturtle()

    #pentru patrat trebuie sa ii zicem noi unde si cum sa mearga, nu exista functie precum circle
    # Pentru un pătrat cu latura de 50:
    for latura in range(4):
        t.forward(50)  # Merge în față 50 de pixeli
        t.left(90)     # Se rotește la 90 de grade (colțul pătratului)
    #facem modelul rotind patratele
    for i in range(36):
        for culoare in culori:
            t.color(culoare)
            for latura in range(4):
                t.forward(60)  # Lungimea laturii pătratului
                t.left(90)     # Unghiul de 90 de grade
            t.left(10)# După ce a desenat un pătrat, se rotește 10 grade pentru a-l desena pe următorul
    t.hideturtle()
turtle.mainloop()