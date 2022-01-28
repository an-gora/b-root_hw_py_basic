class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        # file = open('logging.txt', 'w')
        # file.write(msg)
        with open('logs.txt', 'a') as file_object:
            file_object.write(self.msg + '\n')


for i in range(1, 10):
    try:
        if i % 2 == 0:
            raise CustomException('Item should not be even ')
    except ValueError:
        print("Error type of value!")
    except CustomException as msg:
        print(msg)


