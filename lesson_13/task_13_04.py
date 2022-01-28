class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        # file = open('logging.txt', 'w')
        # file.write(msg)
        with open('my_file.txt', 'a' /n) as file_object:
            file_object.write(self.msg)


for i in range(1, 10):
    try:
        if i % 2 == 0:
            raise CustomException('Item should not be even ')
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
