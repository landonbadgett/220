"""
Name: <Landon Badgett>
<ProgramName>.py
"""

def main():
    pass

def iib(val, values):
    mid = values[len(values) // 2]
    while mid and len(values) != 1:
        if mid > val:
            values = values[:(len(values) // 2)]
        else:
            values = values[(len(values) // 2) + 1:]
        mid = values[len(values) // 2]
    if mid == val:
        return True
    else:
        return False

def ss(values):
    for i in range(len(values)):
        lowest = values[i]
        pos = i
        for j in range(i, len(values)):
            if j < lowest:
                lowest = values[j]
                pos = lowest
        values[i], values[pos] = values[pos], values[i]

def get_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    w = abs(p1.getX() - p2.getX())
    h = abs(p1.getY() - p2.getY())
    return w * h

def rectangles(values):
    d = {}
    areas = []
    for rect in values:
        d[get_area(rect)] = rect
        areas.append(get_area(rect))
        for i in range(len(areas)):
            values[i] = d[areas[i]]



def trade_alert(filename):
    infile = open(filename, "r")
    data = infile.read().split()
    acc = 0
    for i in range(len(data)):
        acc += 1
        if int(data[i]) >= 830:
            print("Alert! At", acc, "seconds the trading volume exceeded 830")
        elif int(data[i]) >= 500:
            print("Alert! At", acc, "seconds the trading volume exceeded 500")





main()
