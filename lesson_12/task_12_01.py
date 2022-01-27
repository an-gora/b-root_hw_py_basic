# Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and
# add them as attributes. Make another method called talk() which makes prints a greeting from the person containing,
# for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.

class Person():
    def __init__(self, fistname: str, lastname: str, age: int):
        self.firstname = fistname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f'Hello! My name is {self.firstname}  {self.lastname} and I am {self.age} years old')

new_person = Person ('Bob', 'Brown', 39)
new_person.talk()
