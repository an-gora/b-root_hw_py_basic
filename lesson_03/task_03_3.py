def make_operation(operator: str, *args: int) -> int:
    result = 0
    if operator == '+':
        for num in args:
            result += num
    elif operator == '-':
        for num in args:
            result -= num
    elif operator == '*':
        result = 1
        for num in args:
            result = result * num
    return result

if __name__ == '__main__':
    print(make_operation('+', 100, 5, 5, 7, 8, 700))
