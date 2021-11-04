from random import randint
from rectangle import Rectangle
from circle import Circle
from triangle import Triangle
from typing import List
import typing

class Container:
    def __init__(self):
        self.store = []

    def in_random(self, shape_num: int):
        for i in range(shape_num):
            figure_index = randint(1, 3)
            if figure_index == 1:
                shape = Rectangle()
                shape.random_parameters()
                self.store.append(shape)
            if figure_index == 2:
                shape = Triangle()
                shape.random_parameters()
                self.store.append(shape)
            if figure_index == 3:
                shape = Circle()
                shape.random_parameters()
                self.store.append(shape)

    def read_file(self, filename: str):
        with open(filename, 'r') as file:
            figure_index = int(file.readline())
            while figure_index != 0:
                if figure_index == 1:
                    shape = Rectangle()
                    shape.from_file(int_array=list(map(lambda x: int(x), file.readline().split())))
                    self.store.append(shape)
                if figure_index == 2:
                    shape = Triangle()
                    shape.from_file(list(map(lambda x: int(x), file.readline().split())))
                    self.store.append(shape)
                if figure_index == 3:
                    shape = Circle()
                    shape.from_file(list(map(lambda x: int(x), file.readline().split())))
                    self.store.append(shape)
                figure_index = int(file.readline())

    def print(self):
        print("Container is store", len(self.store), "shapes:")
        for shape in self.store:
            shape.print()

    def write(self, ostream: typing.IO):
        ostream.write(f"Container is store {len(self.store)} shapes:\n")
        for shape in self.store:
            shape.write(ostream)
            ostream.write("\n")

    def shell_sort(self):
        d = len(self.store) // 2
        while d != 0:
            for i in range(d, len(self.store), d):
                j = i
                while j > 0 and (self.store[j - d].area() > self.store[j].area()):
                    self.store[j - d], self.store[j] = self.store[j], self.store[j - d]
                    j -= d
            d //= 2
