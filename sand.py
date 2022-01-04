# # # def print_tree(n):
# # #     for i in range(n):
# # #         for j in range(n - 1):
# # #             print(' ', end='')
# # #         for k in range(2 * i + 1):
# # #             print('*', end='')
# # #         print()
# # # print_tree(7)
# # # def custom_numbers(a,pow=3):
# # #     return a**pow
# # # print(custom_numbers(2,10))
# # #
# # # def custom_print(*args):
# # #     print(f'print got {len(args)} inside args tiple:', args)
# # #
# # # custom_print(1,2,3,4)
# # # custom_print(1,2,3,4,5,6,6,7,8,9)
# # # def custom_print(**kwargs):
# # #     print(f'print got {len(kwargs)} inside args tiple:', kwargs)
# # # custom_print(name='bathman', enemy='jocker')
# # #
# # #
# # # x = 11111
# # #
# # #
# # # def test2(x):
# # #     x = 101
# # #     x += 1
# # #     print('here is x=', x)
# # #
# # #
# # # test2(x)
# # # print('global', x)
# # #
# # #
# # # def test3():
# # #     print('here is x inside func', x)
# # #
# # #
# # # test3()
# # #
# # #
# # # def test4():
# # #     global x
# # #     x += 1
# # #     print('here is x inside func test4', x)
# # #
# # #
# # # test4()
# # # print(x)
# # #
# # #
# # # def test5(x):
# # #     x += 45
# # #     return x
# # #
# # #
# # # x = test5(x)
# # # print(x)
# # #
# # #
# # # print (2**2)
# # # print(11/2)
# # # print(abs(-1))
# # # print(type(1))
# # # print(round(5.455555,2))
# # #
# # # x = 10
# # # y = 2
# # # operations = ['addition', 'subtraction', 'division', 'multiplictaion',
# # #               'exponent', 'modulus', 'floor division']
# # # results = list()
# # # # results = []
# # # results[0] = x + y
# # # results[1] = x - y
# # # results[2] = x / y
# # # results[3] = x * y
# # # results[4] = x * y
# # # results[5] = abs(x, y)
# # # results[6] = x // y
# # # operation_and_result = list()
# # # # operation_and_result = []
# # # for i in range(len(operations)):
# # #     print (operation_and_result[i] = ('%s %f' % (operations[i],
# # #                                                 results[i])))
# # # '''
# # #
# # # # operations = ['addition', 'subtraction', 'division', 'multiplictaion',
# # # #               'exponent', 'modulus', 'floor division']
# # # # results = [1, 2, 3, 4, 5, 6, 7]
# # # # operation_and_results = []
# # # # for i in operation_and_results:
# # # #     operation_and_results[i] = 1 + i
# # # #
# # # # print(operation_and_results)
# # # #
# # #
# # # name = 'Dostoyevsky'
# # # lenght_of_name = len(name)
# # # print(lenght_of_name)
# #
# # # import random
# # #
# # # print('lets play')
# # # player = input('choose r s or p ')
# # #
# # # if player == 'r' or player == 'p' or player == 's':
# # #     computer = random.randint(1, 3)
# # #     if (computer == 1 and player == 'r' or computer == 2 and
# # #             player == 'p' or computer == 3 and player == 's'):
# # #         print('it is draw')
# # #     elif (computer == 1 and player == 'p' or
# # #           computer == 2 and player == 's' or
# # #           computer == 3 and player == 'r'):
# # #         print("cong, you win")
# # #     else:
# # #         print('you lost')
# # # else:
# # #     print('wrong format')
# # # from random import random
# # #
# # # print([int(1./random.random()) for i in range(10)])
# #
# # # import random
# # #
# # # slovo = 'Привет'
# # # slovo_list = list(slovo)
# # # abrakadabra = random.sample(slovo_list,  len(slovo_list))
# # #
# # # print(abrakadabra)
# #
# # a = 'apples'
# # b = 'pears'
# # c = ['grapes', 'bananas', 'kiwis']
# #
# #
# # def convert(a):
# #     if type(a) == list:
# #         return a
# #     elif type(a) == str:
# #         return [a]
# #
# #
# # d = []
# # for i in [a, b, c]:
# #     d.extend(convert(i))
# # print(d)
# # try:
# #     [1, 2, 3][4]
# # except:
# #     print('oops error')
# #     raise
#
# # try:
# #     raise Exception('spam')
# # except Exception as inst:
# #     print (type(inst))
# #     print(inst.args)
# #     print((inst))
# # from random import random
# #
# # random_number = random.randint(1, 10)
# # print(random_number)

# x = 0
# y = (0,)
#
# print(list(range(-10, 0, 1)))
#
# l = [1, 2, 3]
# for i in range(len(l)):
#     print(l[i])

# username = input('name')
#
# with open('user_info.txt', 'w') as file_object:
#     file_object.write(username)


# with open('user_info.txt') as file_object:
#     username = file_object.read()
#
# print('hello ' + username)

# import json
# stock = {}
# stock={"banana": 6, "apple": 0, "orange": 32, "pear": 15}
# # prices={"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
#
# with open('stock.json', 'w') as file_object:
#     json.dump(stock, file_object)
#
# import json
#
# with open('stock.json') as file_object:
#     stock = json.load(file_object)
#
# for k, v in stock.items():
#     print(k, ':', v)


def make_operation(operator: str, *args: int) -> int:
    result = 0
    if operator == "+":
        for num in args:
            result += num
            return result
    elif operator == "-":
        for num in args:
            result -= num
            return result
    elif operator == "*":
        result = 1
        for num in args:
            result = result * num
            return result

    else:
        print("wrong value")


if __name__ == "__main__":
    print(make_operation("*", 98, 34, 67, 98, 67))

