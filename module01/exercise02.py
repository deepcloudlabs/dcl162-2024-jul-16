class vehicle:
    """
        members:
        1. attributes         -> licence_plate, capacity, load
        2. (business) methods -> load, unload, constructor (__init__) -> create object
    """

    def __init__(self, licence_plate: str, capacity: float = 1_000) -> None:
        self.licence_plate = licence_plate
        self.capacity = capacity
        self.current_load = 0

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
        if self.current_load + weight > self.capacity:
            raise ValueError(f"Current load ({self.current_load}) exceeds capacity ({weight}).")
        self.current_load += weight
        return self.current_load

    def unload(self, weight: float) -> float:
        # validation
        if weight <= 0:
            raise ValueError(f"weight ({weight}) must be a positive number.")
        if weight > self.current_load:
            raise ValueError(f"weight ({weight}) should not exceed current load ({self.current_load}).")
        self.current_load -= weight
        return self.current_load


vehicle1 = vehicle(licence_plate="34abc42", capacity=5_000)
vehicle2 = vehicle("06def49", 2_500)
vehicle3 = vehicle(capacity=8_000, licence_plate="07mn108")
