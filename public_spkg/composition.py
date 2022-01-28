class Car:
    class __Engine:
        def __init__(self, c):
            self.hourly_smthg = 2*c

    def __init__(self, a, b):
        self.average_smthg = 0, 4 * a
        self.engine = Car.__Engine(b)


delorean = Car(250, 4)
print(type(delorean))
print(type(delorean.engine))

# new_engine = Car.__Engine(5)

