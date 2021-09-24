"""
Name: Landon Badgett
mean.py

Problem: Create a program to calculate means

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
#1. What will the program do?
#Collect the RMS, Harmonic, and Geometric means based on different inputs given by a user
#2. What will be the inputs and outputs?
#Inputs: Number of terms, values of terms
#Outputs: The different means
#3. What is a step-by-step list of what the program must do, aka an algorithm?
#Create a loop to iterate through the list of inputs given by the user for n number of terms
#Pass it through the apppropriate mean equation
#Print the output

import math


def rms_average():
    n = eval(input("Enter the number of terms: "))
    acc = 0
    for i in range(n):
        values = eval(input("Enter value " + str(i + 1)))
        values_squared = values ** 2
        acc += values_squared
        average = acc / n
        rms = math.sqrt(average)
    print(round(rms, 3))
#rms_average()

def harmonic_mean():
    n = eval(input("Enter the number of terms: "))
    acc = 0
    for i in range(n):
        values = eval(input("Enter value " + str(i + 1)))
        acc += 1 / values
        harm = n / acc
    print(harm)

def geometric_mean():
    n = eval(input("Enter the number of terms: "))
    acc = 1
    for i in range(n):
        values = eval(input("Enter value " + str(i + 1)))
        acc *= values
        geo = acc ** (1/n)
    print(round(geo, 3))

def main():
    rms_average()
    harmonic_mean()
    geometric_mean()
main()
