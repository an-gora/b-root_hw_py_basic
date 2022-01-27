class Car:
    amount_of_instances = 0

    def __init__(self, color):
        self.color = color
        Car.amount_of_instances +=1

car_1 = Car('green')
car_2 = Car('blue')
print(Car.amount_of_instances)

