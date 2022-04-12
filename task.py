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