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

# a = float(0)
# print(a)
#
#
# def filter_by_name():
#     mymovie = input('what movie are you looking for? ')
#     for movie, movieinfo in list_of_media.items():
#         if movieinfo['title'] == mymovie:
#             year = movieinfo['year']
#             genre = movieinfo['genre']
#             rating = movieinfo['rating']
#             print(f'Here is info about movie {mymovie}: \n'
#                   f'released at {year}\n'
#                   f'genre is {genre}\n'
#                   f'rating is {rating}')
#
# def filter_by_name():
#     movie = input('what movie are you looking for? ')
#     has_such_movie = []
#     for k_1 in list_of_media.keys():
#         mydict = list_of_media[k_1]
#         if ([v for k, v in mydict.items() if k == 'title' and v == movie]):
#             has_such_movie.append(mydict)
#         else:
#             continue
#     if has_such_movie:
#         print(f'here is info about {movie} movie: \n {mydict}')
#     else:
#         print(f'hhhmmmm...seems here is no movie with name {movie}')


# myvar = Wowclass([1,2,3,4,5])
# @myvar
# def ho():
#   return 5
# for i in myvar:
#   print(i)
# myvar = myvar + Wowclass([6,7])
# class School:
#    class_number = Wowclass([1,2,3,4,5,6,7,8,9,10,11])
# s1 = School()
# s1.class_number = 5 # OK
# s1.class_number=12 # raise Exception

# def a_decorator_passing_arbitrary_arguments(function_to_decorate):
#     def a_wrapper_accepting_arbitrary_arguments(a, b):
#         function_to_decorate(a, b)
#     return a_wrapper_accepting_arbitrary_arguments
#
# def func(a,b):
#     print(a,b)
#
# a_decorator_passing_arbitrary_arguments(func(1,3))

# class MyClass():
#
#     def __init(self):
#         pass
#
#     def __str__(self):
#         pass
#
# def method_friendly_decorator(method_to_decorate):
#     def wrapper(lie):
#         my_list = [1,2,3,4,5]
#         for i in my_list:
#             lie += i
#         print(lie+method_to_decorate())
#     return wrapper
#
# @method_friendly_decorator
# def method_to_decorate():
#     return 5
#
# print(method_friendly_decorator(method_to_decorate()))

# with open('file.txt', 'w') as f:
#     f.write('hello')


# def method_friendly_decorator(method_to_decorate):
#     def wrapper(self, lie):
#         lie -= 3
#         return method_to_decorate(self, lie)
#     return wrapper

#
# class Lucy:
#     def __init__(self):
#         self.age = 32
#
#     def method_friendly_decorator(method_to_decorate):
#         def wrapper(self, lie):
#             lie -= 3
#             return method_to_decorate(self, lie)
#
#         return wrapper
#
#     @method_friendly_decorator
#     def sayYourAge(self, lie):
#         print("Мне {} лет, а ты бы сколько дал?".format(self.age + lie))
#
#
# l=Lucy()
# l.sayYourAge(-3)


# from functools import wraps
#
# class Repeater:
# def __init__(self, n):
# self.n = n
# def __call__(self, f):
# @wraps(f)
# def wrapper(*args, **kwargs):
# for _ in range(self.n):
# f(*args, **kwargs)
# return wrapper
#
# @Repeater(3)
# def foo():
# print('foo')
# foo()


from functools import wraps

class Repeater:
    def __init__(self, list):
        self.list = list

    def __call__(self, f):
        @wraps(f)
        def wrapper(this_list):
            for i in self.this_list:
                f()+i
        return wrapper


a = Repeater([1,2,3,4,5])

@a
def foo():
    print(5)
foo()
