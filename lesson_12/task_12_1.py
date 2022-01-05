class Car():
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.total_driven_km = 0

    def __str__(self, name: str):
        return f
        `{self.__class__.__name__}

    def repaint(self, color):
        self.color = color

    def drive(self, km_driven):
        self.total_driven_km += km_driven


my_car = Car('Volvo', 'V90', '2017', 'black')
# print(my_car.brand)
# print(my_car.model)
# print(my_car.year)
print(my_car)
# print(my_car.color)
# my_car.repaint('green')
# print(my_car.color)
# print(my_car.total_driven_km)
# my_car.drive(1000)
# print(my_car.total_driven_km)
