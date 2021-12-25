# Write a program that takes your name as input, and then your age as input and
# greets you with the following:
# # “Hello <name>, on your next birthday you’ll
# be <age+1> years”

def user_data() -> tuple[str, int]:
    name = input('what is your name? ')
    age = int(input('how old are you? '))
    # return f'Hello, {name}, on your next birthday you will be {age + 1} years'
    return name, int(age)


def gr_print(name, age) -> str:
    print(f'Hello, {name}, on your next birthday you will be {age + 1} years')


def main():
    name, age = user_data()
    gr_print(name, age)
    return gr_print


if __name__ == '__main__':
    main()
