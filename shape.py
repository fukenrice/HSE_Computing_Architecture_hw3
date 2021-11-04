#----------------------------------------------
import typing


class Shape:
    def print(self):
        pass

    def write(self, ostream: typing.IO):
        pass

    def from_file(self, int_array: typing.List[int]):
        pass

    def random_parameters(self):
        pass

    def area(self):
        pass

    @staticmethod
    def get_color(color_index: int):
        if color_index == 1:
            return "red"
        if color_index == 2:
            return "orange"
        if color_index == 3:
            return "yellow"
        if color_index == 4:
            return "green"
        if color_index == 5:
            return "blue"
        if color_index == 6:
            return "dark blue"
        if color_index == 7:
            return "violet"
        return ""
