# Make a program that checks if a string is
# in the right format for a phone number.
# The program should check that the string contains only
# numerical characters and is only 10 characters long.
# Print a suitable message depending on
# the outcome of the string evaluation.
from typing import TypeAlias

T_PHONE: TypeAlias = float | int | str


def is_phone_number(phone_number: T_PHONE) -> bool:
    if phone_number.isdigit() and len(phone_number) == 10:
        return True
    else:
        return False


def print_message(number_or_not: bool) -> str:
    if number_or_not:
        return ('string is in the right format for '
                'a phone number')
    else:
        return ('string is NOT in the right format for '
                'a phone number')


if __name__ == '__main__':
    print(print_message(is_phone_number('klkjkj')))
