from typing import TypeAlias

# Write a program that asks the answer for a mathematical expression,
# checks whether the user is right
# or wrong, and then responds with a message accordingly.

T_MY_EXPRESSION: TypeAlias = float | int | str


# обработать исключения - когда операция не распознана

def math_expression(first_digit, second_digit, operation: T_MY_EXPRESSION, result=None):
    result
    expression = str(first_digit) + operation + str(second_digit)
    if operation == "+":
        result = first_digit + second_digit
    elif operation == "-":
        result = first_digit - second_digit
    elif operation == "/":
        result = first_digit / second_digit
    elif operation == "*":
        result = first_digit * second_digit
    else:
        result = 'do not know about that operation'
    return [result, expression]


def math_quiz(my_list) -> str:
    player_number = int(input(f'do you know resul of {my_list[1]} expression? :  '))
    if int(my_list[0]) == player_number:
        return 'good job!'
    else:
        return 'bad baaad answer'


if __name__ == '__main__':
    print(math_quiz(math_expression(47, 5, '*')))
