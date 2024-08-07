import math


class square:
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
        return self.__edge * self.__edge


class cube(square):  # cube is a square
    def __init__(self, x, y, z, edge):
        super().__init__(x, y, edge)
        self.__z = z

    @property
    def z(self) -> float:
        return self.__z

    def __str__(self) -> str:
        return f"cube({super().x}, {super().y}, {self.z}, {super().edge})"

    def area(self) -> float:
        return 6.0 * super().area()  # delegate to square's area
        # return 6.0 * super().edge * super().edge

    def volume(self) -> float:
        return super().edge ** 3


class circle(square):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    @property
    def radius(self) -> float:
        return super().edge

    def area(self) -> float:
        return math.pi * self.radius * self.radius


class sphere(circle):
    def __init__(self, x, y, z, radius):
        super().__init__(x, y, radius)
        self.__z = z

    def area(self) -> float:
        return 4.0 * super().area()  # delegate to circle's area

    def volume(self) -> float:
        return (4.0 * math.pi * super().area()) / 3.0


sq1 = square(1.0, 1.0, 5.0)
c1 = circle(1.0, 1.0, 5.0)
cube1 = cube(2.0, 3.0, 4.0, 5.0)
sp1 = sphere(2.0, 3.0, 4.0, 5.0)
print(sq1)
print(cube1)
print(f"area of sq1: {sq1.area()}")
print(f"area of c1: {c1.area()}")
print(f"area of cube1: {cube1.area()}")
print(f"area of sp1: {sp1.area()}")
# error: print(f"volume of sq1: {sq1.volume()}")
print(f"volume of cube1: {cube1.volume()}")
print(f"volume of sp1: {cube1.volume()}")
print(f"volume of sp1: {sp1.volume()}")
