# Create a program that reads an input string and then creates and
# prints 5 random strings from characters of the input string.
# For example, the program obtained the word ‘hello’,
# so it should print 5 random strings(words) that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’
# -> ‘hlelo’, ‘olelh’, ‘loleh’ …
# Tips: Use random module to get random char from string)

import random


def worlds_combination():
    origin = input('give me one world: ')
    list_of_random = ...
    for i in origin:
        list_of_random = list_of_random + random.randint(1, len(origin))
    return list_of_random

    # origin = input('give me one world: ')
    # range_of_random = len(origin)
    # amount_of_str = 5
    # list_of_str = []
    # random_list = []
    # for i in origin:
    #     another_new_str = []
    #     for j in range_of_random:
    #         random_list[j] = random.randint(1, range_of_random)
    #         another_new_str[j] = another_new_str[j] + origin[random_list[j]]
    #     list_of_str[i] = list_of_str[i] + "1"
    # return list_of_str
    #
    # # while i > 0:
    # #     random_list = []
    # #     while j > 0:
    # #         random_list[j] = random.randint(1, range_of_random)
    # #         another_new_str[j] += origin[random_list[j]]
    # #     list_of_str[i] = another_new_str[i]
    # # return list_of_str


if __name__ == '__main__':
    print(worlds_combination())
