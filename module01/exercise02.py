from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    WHITE = 4
    BLACK = 5


class OverCapacityError(Exception):
    """
    Business Exception
    OverCapacityError is an Exception
    OverCapacityError: subclass/derived class
    Exception: super class/base class
    Raised when an over-capacity error is encountered.
    """

    def __init__(self, message: str, over_weight: float):
        super().__init__()
        self.message = message
        self.__over_weight = over_weight

    @property
    def over_weight(self):
        return self.__over_weight

    def __str__(self) -> str:
        return f'OverCapacityError [{self.message}]: {self.over_weight}'


class vehicle(object):
    """
        members:
        1. attributes         -> licence_plate, capacity, load
        2. (business) methods -> load, unload, constructor (__init__) -> create object
                                 getter/setter
                                 __str__: def __str__ object -> str
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
    def capacity(self) -> float:
        return self.__capacity

    @property
    def current_load(self) -> float:
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
            over_weight = self.__current_load + weight - self.__capacity
            message = f"Current load ({self.__current_load}) exceeds capacity ({self.__capacity})."
            raise OverCapacityError(message=message, over_weight=over_weight)
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

    def __str__(self) -> str:
        return f"vehicle [license_plate: {self.licence_plate}, capacity: {self.capacity}, current_load: {self.current_load}, color: {self.color}]"


try:
    vehicle1 = vehicle(licence_plate="34abc42", capacity=5_000)
    vehicle2 = vehicle("06def49", 2_500)
    vehicle3 = vehicle(capacity=8_000, licence_plate="07mn108")
    vehicle2.load(1_000)
    vehicle3.load(2_000)
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
    print(vehicle1)  # F7BE<__main__.vehicle object at 0x0000020876B0>
    print(str(vehicle1))
except OverCapacityError as oce:
    print(oce)
except ValueError as ve:
    print(ve)
finally:
    print(f"unload all loads from vehicle1: {vehicle1.unload(vehicle1.current_load)}")
    print(f"unload all loads from vehicle2: {vehicle2.unload(vehicle2.current_load)}")
    print(f"unload all loads from vehicle3: {vehicle3.unload(vehicle3.current_load)}")
