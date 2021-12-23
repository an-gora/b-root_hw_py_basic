# def print_tree(n):
#     for i in range(n):
#         for j in range(n - 1):
#             print(' ', end='')
#         for k in range(2 * i + 1):
#             print('*', end='')
#         print()
# print_tree(7)
# def custom_numbers(a,pow=3):
#     return a**pow
# print(custom_numbers(2,10))
#
# def custom_print(*args):
#     print(f'print got {len(args)} inside args tiple:', args)
#
# custom_print(1,2,3,4)
# custom_print(1,2,3,4,5,6,6,7,8,9)
# def custom_print(**kwargs):
#     print(f'print got {len(kwargs)} inside args tiple:', kwargs)
# custom_print(name='bathman', enemy='jocker')
#
#
# x = 11111
#
#
# def test2(x):
#     x = 101
#     x += 1
#     print('here is x=', x)
#
#
# test2(x)
# print('global', x)
#
#
# def test3():
#     print('here is x inside func', x)
#
#
# test3()
#
#
# def test4():
#     global x
#     x += 1
#     print('here is x inside func test4', x)
#
#
# test4()
# print(x)
#
#
# def test5(x):
#     x += 45
#     return x
#
#
# x = test5(x)
# print(x)
#
#
# print (2**2)
# print(11/2)
# print(abs(-1))
# print(type(1))
# print(round(5.455555,2))
#
# x = 10
# y = 2
# operations = ['addition', 'subtraction', 'division', 'multiplictaion',
#               'exponent', 'modulus', 'floor division']
# results = list()
# # results = []
# results[0] = x + y
# results[1] = x - y
# results[2] = x / y
# results[3] = x * y
# results[4] = x * y
# results[5] = abs(x, y)
# results[6] = x // y
# operation_and_result = list()
# # operation_and_result = []
# for i in range(len(operations)):
#     print (operation_and_result[i] = ('%s %f' % (operations[i],
#                                                 results[i])))
# '''
#
# # operations = ['addition', 'subtraction', 'division', 'multiplictaion',
# #               'exponent', 'modulus', 'floor division']
# # results = [1, 2, 3, 4, 5, 6, 7]
# # operation_and_results = []
# # for i in operation_and_results:
# #     operation_and_results[i] = 1 + i
# #
# # print(operation_and_results)
# #
#
# name = 'Dostoyevsky'
# lenght_of_name = len(name)
# print(lenght_of_name)
