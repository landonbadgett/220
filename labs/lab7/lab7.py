"""
Name: <Landon Badgett>
Partner: <Tucker Kilcoyne>
<ProgramName>.py
"""
import math
def cash_conversion():
    x = int(input("Enter an integer: "))
    y = ("{:.2f}".format(x))
    print("$" + y)

def encode():
    s = str(input("Enter the string: "))
    key = eval(input("Enter the key: "))
    acc = ""
    for c in s:
        acc += chr((ord(c) - 97 + key) % 26 + 97)
    print (acc)

def sphere_area(radius):
    area = 4 * math.pi * (radius ** 2)
    return area

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

def sum_n(n):
    acc = 0
    for i in range(n):
        acc += i
    return acc

def sum_n_cubes(n):
    acc = 0
    for i in range (n):
        acc += i ** 3
    return acc

def encode_better():
    s = input("Enter a string: ")
    k = input("Enter a key: ")
    acc = " "
    for i in range(len(s)):
        c = ord(s[i])
        key = (k[i])
        key = ord(key) - 97
        c = c + key
        new_c = chr(c)
        acc += new_c
    print (acc)



def main():
    cash_conversion()
    encode()
    print (sphere_area(3))
    print (sphere_volume(3))
    print (sum_n(3))
    print (sum_n_cubes(3))
    encode_better()

    pass


main()
