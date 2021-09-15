"""
Name: <Landon Badgett>
<lab3>.py
"""
def average():
    n = int(input("Enter the number of grades: "))
    acc = 0
    for i in range(n):
        grades = int(input("Enter your grade on HW" + str(i + 1)))
        acc += grades
    HWaverage = acc / n
    print (HWaverage)
average()

def tip_jar():
    acc = 0
    for i in range(5):
        donation = eval(input("Enter the amount of donation: "))
        acc += donation
    print (acc)
tip_jar()

def newton():
    x = eval(input("What number is X? "))
    refine = eval(input("How many times to improve the approximation?"))
    approx = x/2
    for i in range (refine):
        approx = (approx + (x/approx)) / 2
    print (approx)
newton()

def sequence():
    x = eval(input("Enter number of terms in a series: "))
    for i in range (1, x+1):
        y =(1 + (i//2 * 2))
        print(y)
sequence()

def pi():
    n = eval(input("Enter the number of terms in a series"))
    acc = 1
    for i in range (n):
        num = (2 + (i//2 * 2))
        denom = (1+ (i + 1)//2 * 2)
        acc *= num/denom
    print (acc * 2)
pi()

