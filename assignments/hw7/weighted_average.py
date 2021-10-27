"""
Name: Landon Badgett
weighted_average.py

Problem: Create a program to calculate means

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def weighted_average(in_file_name, out_file_name):
    data = open(in_file_name, 'r')
    average = open(out_file_name, 'w')

    for line in data:
        new_grades = line.split(":")
        name = new_grades[0]
        grades = new_grades[1].strip().split()

        total_weight = 0
        acc = 0
        for i in range(0, len(grades), 2):
            weight = eval(grades[i])
            final_grade = (int(grades[i]) * int(grades[i+1])) / 100
            total_weight += weight
            acc += final_grade

        if total_weight == 100:
                average.write(name + "'s average: " + str(round(acc, 1)) + '\n')

        elif total_weight > 100:
                average.write(name + "'s average: Error: The weights are more than 100." + '\n')


        else:
                average.write(name + "'s average: Error: The weights are less than 100." + '\n')


    data.close()
    average.close()

def main():
    weighted_average('grades.txt', 'avg.txt')

if __name__ == '__main__':
    main()










