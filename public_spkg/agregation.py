class Engine:
    def __init__(self, capacity):
        self.hourly_consumption = 2*capacity


class Car:
    def __init__(self, max_speed, capacity):
        self.average_speed = 0,4 * max_speed
        self.engine = Engine(capacity)


delorean = Car(250, 4)
print(type(delorean))
print(type(delorean.engine))

# new_engine = Engine(5)
# print(type(new_engine))