'''def print_tree(n):
    for i in range(n):
        for j in range(n - 1):
            print(' ', end='')
        for k in range(2 * i + 1):
            print('*', end='')
        print()
print_tree(7)
def custom_numbers(a,pow=3):
    return a**pow
print(custom_numbers(2,10))

def custom_print(*args):
    print(f'print got {len(args)} inside args tiple:', args)

custom_print(1,2,3,4)
custom_print(1,2,3,4,5,6,6,7,8,9)
def custom_print(**kwargs):
    print(f'print got {len(kwargs)} inside args tiple:', kwargs)
custom_print(name='bathman', enemy='jocker')
'''

x = 11111


def test2(x):
    x = 101
    x += 1
    print('here is x=', x)


test2(x)
print('global', x)


def test3():
    print('here is x inside func', x)


test3()


def test4():
    global x
    x += 1
    print('here is x inside func test4', x)


test4()
print(x)


def test5(x):
    x += 45
    return x


x = test5(x)
print(x)
