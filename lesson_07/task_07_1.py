# Write a program that generates a random number
# between 1 and 10 and lets the user guess
# what number was generated. The result
# should be sent back to the user via a print statement.

import random


def guess_number() -> bool:
    random_number = random.randint(1, 10)
    player_number = input('try to guess number between 1 and 10: ')
    if random_number == player_number:
        return True
    else:
        return False


def print_result_of_the_game(result: bool) -> str:
    if result:
        print('congratulation! you are winner!')
    else:
        print('sorry, you lost...')


if __name__ == '__main__':
    print_result_of_the_game(guess_number())
