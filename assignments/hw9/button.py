"""
Name: Landon Badgett
button.py

Problem: Create a class for the three_button_game.py

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import Text

class Button:

    def __init__(self, shape, label):
        self.shape = shape
        self.label = label
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        x_1 = self.shape.getP1().getX()
        x_2 = self.shape.getP2().getX()
        p_x = point.getX()

        y_1 = self.shape.getP1().getY()
        y_2 = self.shape.getP2().getY()
        p_y = point.getY()
        return x_1 <= p_x <= x_2 and y_1 <= p_y <= y_2

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label2):
        self.text.setText(label2)
