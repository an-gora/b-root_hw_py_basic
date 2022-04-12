# class ContManager(object):
#     def __init__(self):
#         print('__init__')
#
#     def __enter__(self):
#         print('__enter__')
#         return self
#
#     def __exit__(self, type, value, traceback):
#         print('__exit__:', type, value)
#         return True  # Подавить исключение
#
#     def __del__(self):
#         print('__del__', self)
#
#
# with ContManager() as c:
#     print('Делаем что-нибудь с c:', c)
#     raise RuntimeError()
# print('завершаем действия')
#
# print('Выполнено')


# import datetime

# class ContManager(object):
#     def __init__(self):
#         print('__init__')
#
#     def __enter__(self):
#         print('__enter__')
#         # t1 = datetime.datetime.now()
#         return t1
#
#     def __exit__(self, type, value, traceback):
#         print('__exit__:', type, value)
#         # t2 = t1 - datetime.datetime.now()
#         return t2  # Подавить исключение
#
#     def __del__(self):
#         print('__del__', self)
#
#
# with ContManager() as c:
#     print('Делаем что-нибудь с c:', c)
#     raise RuntimeError()
# print('завершаем действия')
#
# print('Выполнено')
import datetime


class ContManager(object):
    def __init__(self):
        self.t1 = 0
        self.t2 = 0
        print('__init__')

    def __enter__(self):
        print('__enter__')
        self.t1 = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.t2 = datetime.datetime.now()
        print('__exit__:', type, exc_value)
        return True  # Подавить исключение

    def __del__(self):
        print('__del__', self)


with ContManager() as c:
    print('Делаем что-нибудь с c:', c)
    raise RuntimeError()
print('завершаем действия')

print('Выполнено')