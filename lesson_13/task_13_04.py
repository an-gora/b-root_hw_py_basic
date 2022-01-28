class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        file = open('logging.txt', 'w')
        file.write(msg)
        # with open(r"C:\otus.txt", "w") as file:
        #     for line in lines:
        #         file.write(line + '\n')


a = input('Input integer: ')

try:
    a = int(a)
    if a < 0:
        raise CustomException('You give negative!')
except ValueError:
    print("Error type of value!")
except CustomException as msg:
    print(msg)


# class MyError(Exception):
#     def __init__(self, text):
#         self.txt = text
#
#
# a = input("Input positive integer: ")
#
# try:
#     a = int(a)
#     if a < 0:
#         raise MyError("You give negative!")
# except ValueError:
#     print("Error type of value!")
# except MyError as mr:
#     print(mr)
