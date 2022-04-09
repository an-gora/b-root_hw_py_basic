import random
import uuid


class Equipment:
    rate = 0.01
    rate_of_crash = 0.1
    luck = 0

    def __init__(self, basic_price):
        self.basic_price = basic_price
        self.id = uuid.uuid4()
        self.current_price = self.basic_price
        self.base = 0

    def __str__(self):
        return f'it is {self.__class__.__name__}'

    def is_it_luck(self):
        probability_of_crash = random.randint(1, 100)
        return probability_of_crash > self.luck

    def price_of_current_roll(self):
        return self.basic_price*(self.rate if self.is_it_luck() else self.rate_of_crash)

    def roll(self):
        self.current_price = max(self.current_price - self.price_of_current_roll(), 0)


class Ski(Equipment):
    luck = 8


class Board(Equipment):
    luck = 13


class Sleigh(Equipment):
    luck = 2


class Helmet(Equipment):
    rate = 0
    rate_of_crash = 0


class Human:

    def __init__(self, name):
        self.name = name
        self.id = uuid.uuid4()
        self.list_of_current_equipment = []

    def take_equipment(self, equipment):
        self.list_of_current_equipment.append(equipment)

    def return_equipment(self, base):
        for equipment in self.list_of_current_equipment:
            if equipment.base == base:
                self.list_of_current_equipment.remove(equipment)

    def ride(self):
        for equipment in self.list_of_current_equipment:
            equipment.roll()

class Lift:

    def __init__(self):
        pass




