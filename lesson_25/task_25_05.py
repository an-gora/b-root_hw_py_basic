# def sum_of_digits(digit_string: str) -> int:
#     """
#     >>> sum_of_digits('26') == 8
#     True
#
#     >>> sum_of_digits('test')
#     ValueError("input string must be digit string")


def sum_of_digits(digit_string: str) -> int:
    if int(digit_string) <=9:
        return digit_string
    # return sum_of_digits() + int(digit_string)
    return (int(digit_string))%10 + sum_of_digits((int(digit_string)//10))


print(sum_of_digits('12345'))

