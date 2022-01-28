from abc import ABC, abstractmethod
import inspect

class Vehicle(ABC):
    @abstractmethod
    def __init__(self):
        ...

    def move(self, speed, time):
        ...


class Bike(Vehicle):
    def __init__(self, model: str):
        self.model = model
        self.total_driven = 0

    def move(self, speed, time):
        self.total_driven += speed * time
        return self.total_driven


class MTBike(Bike):
    def __init__(self, model, type_of_riding: str):
        super().__init__(model)
        self.type_of_riding = type_of_riding


class Car(Vehicle):

    def __init__(self, model):
        self.model = model
        self.total_driven = 0

    def move(self, speed: int, time: int):
        self.total_driven += speed * time
        return self.total_driven

class Monst1(MTBike, Car):
    def __init__(self, color, model, type_of_riding: str):
        super().__init__(model, type_of_riding)
        self.color = color
        self.total_driven = 0

class Monst2(Car, MTBike):
    def __init__(self, model):
        super().__init__(model)



#вызов переопределенного метода абстр родителя
# new_car = Car('bla')
# s = new_car.move(100, 3)
# print(s)

# метод класса родителя
# new_mtb = MTBike('model', 'type')
# distance = new_mtb.move(30, 2)
# print(distance)

# print('класс объекта')
# print(type(new_mtb))
# print('класс родителя')
# print(type(new_mtb).__bases__)
# print('все родители')
# print(inspect.getmro(type(new_mtb)))

