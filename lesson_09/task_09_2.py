# Generate 2 lists with the length of 10 with random integers
# from 1 to 10, and make a third list containing the common integers
# between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers
import random


def concat_of_2_lists() -> list[int]:
    i = 10
    first_list = []
    second_list = []
    final_list = set()
    while i > 0:
        random_number_for_first_list = random.randint(1, 10)
        first_list.append(random_number_for_first_list)
        random_number_for_second_list = random.randint(1, 10)
        second_list.append(random_number_for_second_list)
        i -= 1
    for number in first_list:
        if number in second_list:
            final_list.add(number)
    return first_list, second_list, final_list


if __name__ == '__main__':
    print(concat_of_2_lists())
