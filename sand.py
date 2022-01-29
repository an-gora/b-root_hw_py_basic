# class Car:
#     amount_of_instances = 0
#
#     def __init__(self, color):
#         self.color = color
#         Car.amount_of_instances +=1
#
# car_1 = Car('green')
# car_2 = Car('blue')
# print(Car.amount_of_instances)


# Действительно, super() может быть использована вне класса. Пример:
#
# d = Discount()
# print(super(Discount, d).price())

# class O:
#     def method(self):
#         print('I am O')
# class A(O):
#     def method(self):
#         super().method()
#         print('I am A')
# class B(O):
#     def method(self):
#         super().method()
#         print('I am B')
# class C(A, B):
#     def method(self):
#         super().method()
#         print('I am C')
# C().method()

a = float(0)
print(a)