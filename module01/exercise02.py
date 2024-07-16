from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    WHITE = 4
    BLACK = 5


class vehicle:
    """
        members:
        1. attributes         -> licence_plate, capacity, load
        2. (business) methods -> load, unload, constructor (__init__) -> create object
    """

    def __init__(self, licence_plate: str, capacity: float = 1_000, color: Color = Color.RED) -> None:
        self.__licence_plate = licence_plate
        self.__capacity = capacity
        self.__current_load = 0
        self.__color = color

    @property
    def licence_plate(self) -> str:
        return self.__licence_plate

    @property
    def capacity(self) -> str:
        return self.__capacity

    @property
    def current_load(self) -> str:
        return self.__current_load

    @property  # getter
    def color(self) -> Color:
        return self.__color

    @color.setter  # setter
    def color(self, new_color: Color) -> None:
        self.__color = new_color

    def load(self, weight: float) -> float:
        """
        business method: loads some weight to the vehicle
        :param weight: weight in kg
        :return: returns current weight in kg
        """
        # validation
        if weight <= 0:
            raise ValueError(f"weight ({weight}) must be a positive number.")
        # business rule
        if self.__current_load + weight > self.__capacity:
            raise ValueError(f"Current load ({self.__current_load}) exceeds capacity ({self.__capacity}).")
        self.__current_load += weight
        return self.__current_load

    def unload(self, weight: float) -> float:
        # validation
        if weight <= 0:
            raise ValueError(f"weight ({weight}) must be a positive number.")
        if weight > self.__current_load:
            raise ValueError(f"weight ({weight}) should not exceed current load ({self.__current_load}).")
        self.__current_load -= weight
        return self.__current_load


vehicle1 = vehicle(licence_plate="34abc42", capacity=5_000)
vehicle2 = vehicle("06def49", 2_500)
vehicle3 = vehicle(capacity=8_000, licence_plate="07mn108")
print(f"vehicle1's current load: {vehicle1.current_load}")
vehicle1.load(weight=500)
print(f"vehicle1's current load: {vehicle1.current_load}")
vehicle1.load(weight=1_500)
print(f"vehicle1's current load: {vehicle1.current_load}")
vehicle1.load(weight=2_000)
print(f"vehicle1's current load: {vehicle1.current_load}")
vehicle1.color = Color.GREEN
vehicle1.load(weight=1_500)
print(f"vehicle1's current load: {vehicle1.current_load}")
