class Engine:
    def __init__(self, capacity):
        self.hourly_consumption = 2*capacity


class Car:
    def __init__(self, a, b):
        self.average_smthg = 0.4 * a
        self.engine = Engine(b)


delorean = Car(250, 4)
print(type(delorean))
print(type(delorean.engine))
print(delorean.average_smthg)

# new_engine = Engine(5)
# print(type(new_engine))