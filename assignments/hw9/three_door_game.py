"""
Name: Landon Badgett
three_door_game.py

Problem: Create a program to play the three door game

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import randint
from graphics import *
from button import Button

def game():
    win = GraphWin("Three Door Game", 200, 200)
    win.setCoords(0, 0, 10, 10)

    button1 = Rectangle(Point(1, 6), Point(3, 4))
    door1 = Button(button1, "Door 1")
    door1.draw(win)

    button2 = Rectangle(Point(4, 6), Point(6, 4))
    door2 = Button(button2, "Door 2")
    door2.draw(win)

    button3 = Rectangle(Point(7, 6), Point(9, 4))
    door3 = Button(button3, "Door 3")
    door3.draw(win)
    message = Text(Point(5, 9), "I have a secret door")
    message2 = Text(Point(5, 1), "Click to choose my door")
    message.draw(win)
    message2.draw(win)

    x = randint(0, 2)
    doors = [door1, door2, door3]
    rand_door = doors[x]
    p = win.getMouse()
    y = x + 1

    if rand_door.is_clicked(p):
        rand_door.color_button("green")
        message.setText("You win!")
        message2.setText("Click to Close")
    else:
        rand_door.color_button("green")
        message.setText("You lose!")
        message2.setText("Door " + str(y) + " is the secret door")

    win.getMouse()
    win.close()


def main():
    game()


if __name__ == '__main__':
    main()
