# Write a program that takes your name as input, and then your age as input and
# greets you with the following:
# # “Hello <name>, on your next birthday you’ll
# be <age+1> years”

def greetings() -> str:
    name = input('what is your name? ')
    age = int(input('how old are you? '))
    return f'Hello, {name}, on your next birthday you will be {age + 1} years'


if __name__ == '__main__':
    print(greetings())
