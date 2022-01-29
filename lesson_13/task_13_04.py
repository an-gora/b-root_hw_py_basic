class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open('logs.txt', 'a') as file_object:
            file_object.write(self.msg + '\n')


for item in range(1, 10):
    try:
        if item % 2 == 0:
            raise CustomException('Item should not be even ')
    except ValueError:
        print("Error type of value!")
    except CustomException as mssg:
        print(mssg)


