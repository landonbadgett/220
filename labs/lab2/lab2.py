"""
Name: <Landon Badgett>
<lab2>.py
"""
import math
def sum_of_threes():
    bound = int(input("Enter Upper Bound"))
    acc = 0
    for i in range (0,bound +1, 3):
        acc += i
    print(acc)
sum_of_threes()

def multiplication_table():
    for h in range (1,11):
        for l in range (1,11):
            print(h * l, end = " ")
        print()
multiplication_table()

def triangle_area():
    a = int(input("Enter side a"))
    b = int(input("Enter side b"))
    c = int(input("Enter side c"))
    s = (a+b+c)/2
    x = (s*(s-a)*(s-b)*(s-c))
    area = math.sqrt(x)
    print(area)
triangle_area()

def sumSquares():
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))
    acc = 0
    for i in range (start,end+1):
        acc+= (i*i)
    print (acc)
sumSquares()

def power():
    base = int(input("Enter Base: "))
    exp = int(input("Enter exponent: "))
    acc = 1
    for i in range(exp):
        acc *= base
    print (acc)
power()
