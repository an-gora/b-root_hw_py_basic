# Write a function that takes in two numbers from the user
# via input(), call the numbers a and b, and
# then returns the value of squared a divided by b,
# construct a try-except block which raises an exception
# if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).


def catch_me_if_you_can():
    try:
        a = int(input('set a: '))
        b = int(input('set b '))
        a * a / b
    except ValueError:
        return 'values given by the input function are not numbers'
    except ZeroDivisionError:
        return 'division on 0 is impossible'


if __name__ == '__main__':
    print(catch_me_if_you_can())
