"""
Name: Landon Badgett
greeting.py

Problem: Create a greeting card

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import time
from graphics import GraphWin, Point, Line, Polygon, Circle, Text


def main():
    win = GraphWin("Greeting Card", 400, 400)
    win.setCoords(0,0,40,40)
    tp1 = Point(14,20)
    tp2 = Point(26,20)
    tp3 = Point(20,7)
    cp1 = Point(18,20)
    cp2 = Point(22,20)

    triangle = Polygon(tp1, tp2, tp3)
    circle1 = Circle(cp1, 4)
    circle2 = Circle(cp2, 4)
    triangle.setFill("red")
    circle1.setFill("red")
    circle2.setFill("red")
    triangle.setOutline("red")
    circle2.setOutline("red")
    circle1.setOutline("red")
    circle1.draw(win)
    circle2.draw(win)
    triangle.draw(win)
    lp1 = Point(0,0)
    lp2 = Point(5,5)
    line = Line(lp1,lp2)
    line.setArrow("last")
    line.draw(win)

    text_pt = Point(20,35)
    text = Text(text_pt, "Happy Valentines Day!")
    text.setTextColor("black")
    text.draw(win)

    for _ in range(20):
        line.move(2,2)
        time.sleep(.1)

    endtext_pt = Point(20, 5)
    endtext = Text(endtext_pt, "Click Anywhere to close")
    endtext.setTextColor("black")
    endtext.draw(win)

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
