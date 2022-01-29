class Engine:
    def __init__(self, c):
        self.hourly_smth = 2 * c


class Car:
    def __init__(self, a, b, some_engine):
        self.average_smthg = 0.4 * a + b
        self.engine = some_engine


engine = Engine(15)
delorean = Car(250, 4, engine)
print(delorean.engine.hourly_smth)



