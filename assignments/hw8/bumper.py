"""
Name: Landon Badgett
bumpers.py

Problem: Create a program to simulate bumper cars

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint
import time
from graphics import GraphWin, Circle, Point, color_rgb


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(ball1, ball2):
    x_collide = abs(ball1.getCenter().getX() - ball2.getCenter().getX())
    y_collide = abs(ball1.getCenter().getY() - ball2.getCenter().getY())
    radius1 = ball1.getRadius()
    radius2 = ball2.getRadius()
    return bool(x_collide <= (radius1 + radius2) and y_collide <= (radius1 + radius2))


def hit_horizontal(ball, win):
    top = ball.getCenter().getY() + ball.getRadius() >= win.getHeight()
    bottom = ball.getCenter().getY() - ball.getRadius() <= 0
    return bool(top or bottom)


def hit_vertical(ball, win):
    right = ball.getCenter().getX() + ball.getRadius() >= win.getWidth()
    left = ball.getCenter().getX() - ball.getRadius() <= 0
    return bool(right or left)


def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = color_rgb(red, green, blue)
    return color

def bumpers():
    win = GraphWin("Bumpers", 600, 600)
    ball1 = Circle(Point(325, 300), 20)
    ball2 = Circle(Point(275, 300), 20)
    ball1.setFill(get_random_color())
    ball2.setFill(get_random_color())
    ball1.draw(win)
    ball2.draw(win)

    ball1_movement = [get_random(9), get_random(9)]
    ball2_movement = [get_random(9), get_random(9)]

    while True:
        ball1.move(ball1_movement[0], ball1_movement[1])
        ball2.move(ball2_movement[0], ball2_movement[1])

        if did_collide(ball1, ball2):
            ball1_movement[0] = -ball1_movement[0]
            ball1_movement[1] = -ball1_movement[1]
            ball2_movement[0] = -ball2_movement[1]
            ball2_movement[1] = -ball2_movement[1]
        if hit_vertical(ball1, win):
            ball1_movement[0] = -ball1_movement[0]
        if hit_vertical(ball2, win):
            ball2_movement[0] = -ball2_movement[0]
        if hit_horizontal(ball1, win):
            ball1_movement[1] = -ball1_movement[1]
        if hit_horizontal(ball2, win):
            ball2_movement[1] = -ball2_movement[1]


        time.sleep(.01)


def main():
    bumpers()

if __name__ == '__main__':
    main()
