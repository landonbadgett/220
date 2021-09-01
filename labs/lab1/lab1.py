"""<Landon Badgett> lab1.py"""
def cal_area():
    length = 20
    width = 5
    area = length * width
    print ("Area =", area)

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print ("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

def shooting_percentage():
    total_shots = eval(input("Enter the total shots"))
    made_shots = eval(input("Enter the made shots"))
    percentage = total_shots / made_shots
    print("Shooting Percentage = Percentage")

def coffee():
    total_cost = 10.50 * lbs_of_coffee + 0.86 * lbs_of_coffee + 1.5
    lbs_of_coffee = eval(input("Enter pounds of coffee"))

def kilometers_to_miles():
    miles = kilometers/1.61
    kilometers = eval(input("Enter number of kilometers"))


