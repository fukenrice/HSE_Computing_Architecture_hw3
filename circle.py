import math
import random

from shape import *


class Circle(Shape):
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.radius = 0
        self.color = 0

    def from_file(self, int_array):
        self.x1 = int_array[0]
        self.y1 = int_array[1]
        self.radius = int_array[2]
        if self.area() <= 0:
            raise ValueError("Площадь круга меньше нуля.")
        self.color = int_array[3]

    def random_parameters(self):
        self.x1 = random.randint(-100, 100)
        self.y1 = random.randint(-100, 100)
        self.radius = random.randint(1, 100)
        self.color = random.randint(1, 7)

    def print(self):
        print(
            f"It is Circle (x1, y1) = ({self.x1}, {self.y1}), radius = {self.radius},"
            f" color: {Shape.get_color(self.color)}, area = {self.area()}")

    def write(self, ostream):
        ostream.write(
            f"It is Circle (x1, y1) = ({self.x1}, {self.y1}), radius = {self.radius},"
            f" color: {Shape.get_color(self.color)}, area = {self.area()}")

    def area(self):
        return math.pi * math.pow(self.radius, 2)

