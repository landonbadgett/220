"""
Name: <Landon Badgett>
<lab6>.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = str(input("Enter your first and last name: "))
    x = name.split(' ')
    first_name = x[0]
    last_name = x[1]
    print(last_name + (", ") + first_name)

def company_name():
    domain = str(input("Enter the three-part internet domain name: "))
    x = domain.split(".")
    company = x[1]
    print(company)

def initials():
    n = eval(input("How many names will be input? "))
    for i in range(n):
        first_name = str(input("Enter the first name of student " + str(i +1) + ": "))
        last_name = str(input("Enter " + str(first_name) + "'s last name: "))
        x = (first_name[0] + last_name[0])
        print(str(first_name) + "'s initals are " + str(x))

def names():
    full_names = str(input("Enter names (first and last only) separated by commas: "))
    list_split = full_names.split(", ")
    print("The initials are", end = " ")
    for x in list_split:
        name_split = x.split(" ")
        first_name = name_split[0]
        last_name = name_split[1]
        y = (first_name[0] + last_name[0])
        print(y, end = " ")
    print(" ")

def thirds():
    n = eval(input("How many sentences will be input? "))
    for i in range(n):
        x = str(input("Enter the sentence: "))
        length = len(x)
        third = x[2:length:3]
        print(third)

def word_average():
    n = eval(input("How many sentences will be input? "))
    for i in range(n):
        acc = 0
        x = str(input("Enter the sentence: "))
        words = x.split(" ")
        total_words = len(words)
        for j in words:
            total_characters = len(j)
            acc += total_characters
        print(acc / total_words)

def pig_latin():
    x = str(input("Enter the sentence: "))
    words = x.split(" ")
    for word in words:
        word1 = word[1:] + word[0] + "ay"
        word1 = word1.lower()
        print(word1, end = " ")






def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()
    # add other function calls here


main()
