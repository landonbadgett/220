"""
Landon
"""


def main():
    roads = eval(input("Enter the number of roads surveyed: "))
    total = 0
    for i in range(roads):
        acc = 0
        n_days = eval(input("How many days was road "+str(i+1)+" surveyed? "))
        for j in range(n_days):
            n_cars = eval(input("How many cars traveled on day "+str(j+1)+"? "))
            acc += n_cars
            total += n_cars
            average_per_road = total/roads
            solution = acc / n_days
        print("Road " + str(i+1) + " average vehicles per day: " + str(round(solution, 2)))
    print("Total number of vehicles traveled on all roads: " + str(round(total, 2)))
    print("Average number of vehicles per road: " + str(round(average_per_road, 2)))


if __name__ == '__main__':
    main()
