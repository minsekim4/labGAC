import turtle as tu

roo = tu.Turtle()  
wn = tu.Screen()  
wn.bgcolor("black")  
wn.title("Noua Retea Fractala")
roo.speed(0)  # cea mai rapidă viteza în turtle

# 1. Am definit O SINGURĂ funcție recursivă cu parametri pentru unghi și scalare
def draw_fractal(l, unghi, scala):  
    if l < 10:
        return
    else:
        roo.forward(l)
        
        # Ramificația stângă
        roo.left(unghi)
        draw_fractal(l * scala, unghi, scala)
        
        # Ramificația dreaptă (compensăm rotația la stânga și mergem la dreapta)
        roo.right(unghi * 2)  
        draw_fractal(l * scala, unghi, scala)
        
        # Revenim la poziția și unghiul inițial
        roo.left(unghi)
        roo.backward(l)

# 2. Definim straturile rețelei folosind o listă (în loc să scriem codul de 12 ori)
setari_straturi = [
    {"lungime": 30, "culoare": "cyan", "grosime": 1},
    {"lungime": 50, "culoare": "magenta", "grosime": 2},
    {"lungime": 70, "culoare": "yellow", "grosime": 3},
    {"lungime": 90, "culoare": "lightgreen", "grosime": 4}
]

# 3. Generăm rețeaua în cele 4 direcții pentru fiecare strat
# Această buclă înlocuiește tot acel cod imens din scriptul tău original
for strat in setari_straturi:
    for i in range(4):
        roo.pensize(strat["grosime"])
        roo.pencolor(strat["culoare"])
        
        # AICI AM SCHIMBAT FORMA: 
        # Am pus unghiul de 45 de grade și factorul de scalare de 0.65 
        # pentru a genera o cu totul altă formă geometrică (o nouă rețea).
        draw_fractal(strat["lungime"], 45, 0.65)  
        
        roo.right(90)  # Rotim la 90 de grade pentru a desena următoarea direcție

wn.exitonclick()