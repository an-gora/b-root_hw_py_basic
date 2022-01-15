class Car():
    # total_numbers_of_cars = 0
    def __init__(self, brand, model):
        # def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        # self.year = year
        # self.color = color
        # self.total_driven_km = 0
        # Car.total_numbers_of_cars +=1

    @classmethod
    def from_string(cls, data1: str, data2: str):
        return cls(brand=data1, model=data2)

    def __str__(self):
        # return str(self.brand)
        return f'{self.__class__.__name__} {self.model} {self.brand}'

    __repr__ = __str__

    # def repaint(self, color):
    #     self.color = color
    #
    # def drive(self, km_driven):
    #     self.total_driven_km += km_driven


def main():
    my_car = Car('Volvo', 'mymodel')
    print(my_car)
    print(Car.from_string(data1='bmw', data2='newmodel'))


if __name__ == '__main__':
    main()

# my_car = Car('Volvo', 'V90', '2017', 'black')
# print(my_car.__str__())
# print(my_car.brand)
# print(my_car.model)
# print(my_car.year)
# print(my_car)
# print(my_car.color)
# my_car.repaint('green')
# print(my_car.color)
# print(my_car.total_driven_km)
# my_car.drive(1000)
# print(my_car.total_driven_km)
