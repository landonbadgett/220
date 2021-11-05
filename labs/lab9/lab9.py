"""
Name: <Landon Badgett>
<lab9>.py
"""
from graphics import *
import math

def main():
    #addTen()
    #squareEach(x)
    #sumList(x)
    #toNumbers(x)
    #writeSumOfSquares()
    #starter()
    #circleOverlap()
    #leapYear()
    pass

def addTen(x):
    for i in range (len(x)):
        x[i] = x[i] + 10

def squareEach(x):
    for i in range(len(x)):
        x[i] = x[i] ** 2
        pass

def sumList(x):
    acc = 0
    for i in range(len(x)):
        acc += x[i]
    return acc

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])
        pass

def writeSumOfSquares():
    itn = input("Enter the name of the file (at least two numbers on each line): ")
    in_file = open(itn, 'r')
    out_file = open("output.txt", 'w+')
    for line in in_file:
        numbers = line.split(" ")
        toNumbers(numbers)
        squareEach(numbers)
        nums_sum = sumList(numbers)
        out_file.write("sum = " + str(nums_sum) + "\n")

def starter():
    weight = float(input("Enter the weight: "))
    wins = int(input("Enter the amount of wins: "))

    if (weight <= 160 and weight > 150) and wins > 5:
        print("This player is a starter.")

    elif weight > 199 and wins > 20:
        print("This player is a starter.")

    else:
        print("This player is not a starter. ")

def leapYear(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("This is a leap year")
    else:
        print("This is not a leap year")

def circleOverlap():
    win = GraphWin("Circle", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    radius = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    circle = Circle(p1, radius)
    circle.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    radius2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    circle2 = Circle(p3, radius2)
    circle2.draw(win)

    distance = math.sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)

    if distance > radius + radius2:
        txt_pt = Point(400 /2, 400 - 10)
        message1 = Text(txt_pt, "The circles do not overlap")
        message1.draw(win)

    elif distance < radius + radius2:
        txt_pt2 = Point(400/2, 400-10)
        message2 = Text(txt_pt2, "The circles overlap")
        message2.draw(win)

    else:
        print()




    win.getMouse()
    win.close()





main()
