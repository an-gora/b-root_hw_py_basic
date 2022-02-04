# def sum_of_digits(digit_string: str) -> int:
#     """
#     >>> sum_of_digits('26') == 8
#     True
#
#     >>> sum_of_digits('test')
#     ValueError("input string must be digit string")

def sum_of_digits(digit_string: str) -> int:
    if len(digit_string) == 1:
        return digit_string
    return sum_of_digits() + int(digit_string)