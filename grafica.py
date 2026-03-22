from graphics import *
#punct
#def main():
#    win = GraphWin("My Graphics", 300, 250)
#    g = Point(150,150)
#    g.draw(win)
#    win.getMouse()
#    win.close()
#main()

#cerc
#def main():
#    mycolor=color_rgb(200,139,55)
#    win = GraphWin("My Graphics", 300,250)
#    g=Circle(Point(150,155),50)
#    g2=Circle(Point(180,155),33)
#    g.draw(win)
#    g3=Circle(Point(20,70),100)
#    g3.setFill(mycolor)
#    g3.draw(win)
#    g2.draw(win)
#    win.getMouse()
#    win.close()
#
#main()

#patrate
#def main():
#    mycolor=color_rgb(200,139,55)
#    win = GraphWin("My Graphics", 300,250)
#    g=Rectangle(Point(50,50) , Point(80,80))
#    g2=Rectangle(Point(50,50) , Point(100,40))
#    g3=Rectangle(Point(80,50), Point(100,80))
#    g3.setFill(mycolor)
#    g2.setOutline(mycolor)
#    g2.draw(win)
#    g.draw(win)
#    g3.draw(win)
#    win.getMouse()
#    win.close()
#
#main()

def main():
    win = GraphWin("semafor_Octavia", 400, 600)
    # Point(x1, y1) este coltul stanga-sus, Point(x2, y2) este coltul dreapta-jos
    corp = Rectangle(Point(150, 50), Point(250, 350))
    corp.setFill("black") 
    rosu = Circle(Point(200, 100), 40)
    rosu.setFill("red")
    galben = Circle(Point(200, 200), 40)
    galben.setFill("yellow")
    verde = Circle(Point(200, 300), 40)
    verde.setFill("green")
    corp.draw(win)
    rosu.draw(win)
    galben.draw(win)
    verde.draw(win)
    mesaj = Text(Point(200, 450), "Semaforul arata ce trebuie sa faci")
    mesaj.setSize(14)    
    mesaj.setStyle("italic") 
    mesaj.draw(win)

    win.getMouse()
    win.close()    

main()