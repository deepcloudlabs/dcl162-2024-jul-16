"""
abstract class
interface
square -> cube
square -> circle -> sphere
triangle

shape2d -> square
shape2d -> triangle
shape2d -> shape3d -> cube
           shape3d -> sphere
"""
import random


class shape2d:  # interface

    def area(self):
        pass


class shape3d(shape2d):  # interface

    def volume(self):
        pass


class square(shape2d):

    def __init__(self, x: float, y: float, edge: float):
        self.__x = x
        self.__y = y
        self.__edge = edge

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    @property
    def edge(self) -> float:
        return self.__edge

    def __str__(self) -> str:
        return f"square({self.x}, {self.y}, {self.edge})"

    def area(self) -> float:
        print("square::area")
        return self.__edge * self.__edge


class cube(shape3d):
    def __init__(self, x, y, z, edge):
        self.__x = x
        self.__y = z
        self.__z = z
        self.__edge = edge

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    @property
    def edge(self) -> float:
        return self.__edge

    @property
    def z(self) -> float:
        return self.__z

    def __str__(self) -> str:
        return f"cube({super().x}, {super().y}, {self.z}, {super().edge})"

    def area(self) -> float:
        print("cube::area")
        return 6.0 * self.edge * self.edge

    def volume(self) -> float:
        return self.edge ** 3


shape1: shape2d = square(1, 2, 10)
shape2: shape3d = cube(1, 2, 3, 4)
# print(shape1.area())
# print(shape2.area())
# print(shape2.volume())

shape3: shape2d = None
if random.randint(0, 1) == 0:
    shape3 = square(1, 2, 4)
else:
    shape3 = cube(1, 2, 3, 4)
print(type(shape3))
print(shape3.area())
shapes: list[shape2d] = [shape1, shape2, shape3]
total_surface_area = 0
for shape in shapes:
    total_surface_area += shape.area() # polymorphism -> agility
