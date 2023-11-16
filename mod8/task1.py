class Transport():
    def __init__(self, coordinates, speed, brand, year, number):
        self.coordinates = coordinates
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number

    def __str__(self):
        return f'Coordinates: {self.coordinates}, Speed: {self.speed}, Brand: {self.brand}, Year: {self.year}, Number: {self.number}'

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        if (pos_x <= self.x <= pos_x + length) and (pos_y <= self.y <= pos_y + width):
            return True
        else:
            return False


class Passenger():
    def __init__(self):
        self.__passengers_capacity = 0
        self.__number_of_passengers = 0

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self.__number_of_passengers = number_of_passengers


class Cargo():
    def __init__(self):
        self.__carrying = 0

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        self.__carrying = carrying


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self.height = height


class Auto(Transport):
    def __init__(self, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, name, port):
        super().__init__(coordinates, speed, brand, year, number)
        self.name = name
        self.port = port


class Car(Auto):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Bus(Auto, Passenger):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CargoAuto(Auto, Cargo):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Boat(Ship):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PassengerShip(Ship, Passenger):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CargoShip(Ship, Cargo):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Seaplane(Plane, Ship):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Ship(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Plane(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
