from extender import *

#
# def read_file(container: Container, filename):
#     with open(filename, 'r') as file:
#         figure_index = int(file.readline())
#         while figure_index != 0:
#             if figure_index == 1:
#                 shape = Rectangle()
#                 shape.from_file(int_array=list(map(lambda x: int(x), file.readline().split())))
#                 container.store.append(shape)
#             if figure_index == 2:
#                 shape = Triangle()
#                 shape.from_file(list(map(lambda x: int(x), file.readline().split())))
#                 container.store.append(shape)
#             if figure_index == 3:
#                 shape = Circle()
#                 shape.from_file(list(map(lambda x: int(x), file.readline().split())))
#                 container.store.append(shape)
#             figure_index = int(file.readline())
