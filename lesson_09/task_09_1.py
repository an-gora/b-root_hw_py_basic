# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers
import random


def greatest_number():
    i = 10
    list_of_random_numbers = []
    while i > 0:
        random_number = random.randint(1, 10)
        list_of_random_numbers.append(random_number)
        i -= 1
    return max(list_of_random_numbers)


if __name__ == '__main__':
    print(greatest_number())
