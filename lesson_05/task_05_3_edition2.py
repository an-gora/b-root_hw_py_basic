from typing import TypeAlias

T_NUMBER: TypeAlias = float | int
T_RESULT: TypeAlias = dict[str, T_NUMBER]


def task_05_3(x: T_NUMBER, y: T_NUMBER) -> T_RESULT:
    results = {
        'addition': x + y,
        'subtraction': x - y,
        'division': x / y,
        'multiplication': x * y,
        'exponent': x ** y,
        'modulus': x % y,
        'floor division': x // y,
    }
    return results


def dict_print(data: T_RESULT) -> None:
    for operation, result in data.items():
        print(f'result for {operation} is {result}')


if __name__ == '__main__':
    dict_print(task_05_3(100, 9))
