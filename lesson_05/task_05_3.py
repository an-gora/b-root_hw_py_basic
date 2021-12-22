def task_05_3(x: float, y: float) -> list[str]:
    operations = ['addition', 'subtraction', 'division', 'multiplication',
                  'exponent', 'modulus', 'floor division']
    results = []
    # все операции в 1 список обьявить попробовать словать и список списков
    results[0] = x + y
    results[1] = x - y
    results[2] = x / y
    results[3] = x * y
    results[4] = x * y
    results[5] = x % y
    results[6] = x // y
    operation_and_result = []
    for operation, result in zip(operations, results):
        operation_and_result.append(f'result of {operation} is {result}')
        # for i in range(len(operations)):
        #     operation_and_result[i] = ('%s is %f' % (operations[i],
        #                                           results[i]))
    return operation_and_result


if __name__ == '__main__':
    print(task_05_3(100, 9))
