class Engine:
    def __init__(self, c):
        self.hourly_smthg = 2 * c


class Car:
    def __init__(self, a, b):
        self.average_smthg = 0, 4 * a
        self.engine = Engine(b)


delorean = Car(250, 4)

print(delorean.engine.hourly_smthg)

