import math
import random

from shape import *


# ----------------------------------------------
class Triangle(Shape):
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.x3 = 0
        self.y3 = 0
        self.color = 0

    def from_file(self, int_array):
        self.x1 = int_array[0]
        self.y1 = int_array[1]
        self.x2 = int_array[2]
        self.y2 = int_array[3]
        self.x3 = int_array[4]
        self.y3 = int_array[5]
        if self.area() <= 0:
            raise ValueError("Площадь треугольника меньше нуля.")
        self.color = int_array[6]

    def random_parameters(self):
        self.x1 = random.randint(-100, 100)
        self.y1 = random.randint(-100, 100)
        self.x2 = random.randint(-100, 100)
        self.y2 = random.randint(-100, 100)
        self.x3 = random.randint(-100, 100)
        self.y3 = random.randint(-100, 100)
        while self.area() == 0:
            self.x3 = random.randint(-100, 100)
            self.y3 = random.randint(-100, 100)
        self.color = random.randint(1, 7)

    def print(self):
        print(
            f"It is Triangle (x1, y1) = ({self.x1}, {self.y1}), (x2, y2) = ({self.x2}, {self.y2}),"
            f" (x3, y3) = ({self.x3}, {self.y3}), color: {Shape.get_color(self.color)}, area = {self.area()}")

    def write(self, ostream):
        ostream.write(
            f"It is Triangle (x1, y1) = ({self.x1}, {self.y1}), (x2, y2) = ({self.x2}, {self.y2}),"
            f" (x3, y3) = ({self.x3}, {self.y3}), color: {Shape.get_color(self.color)}, area = {self.area()}")

    def area(self):
        a = math.sqrt(math.pow(self.x2 - self.x1, 2) + math.pow(self.y2 - self.y1, 2))
        b = math.sqrt(math.pow(self.x3 - self.x2, 2) + math.pow(self.y3 - self.y2, 2))
        c = math.sqrt(math.pow(self.x1 - self.x3, 2) + math.pow(self.y1 - self.y3, 2))
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
