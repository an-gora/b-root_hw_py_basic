# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student,
# and another one called Teacher. Try to find as many methods and
# attributes as you can which belong to different classes,
# and keep in mind which are common and which are not.
# For example, the name should be a Person attribute,
# while salary should only be available to the teacher.

class Person:
    def __init_(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        
class Student(Person):
    def __init__(self, name, surname, age, gender, current_class):
        super().__init__(self,name, surname, age, gender)
        self.current_class = current_class
        
    def go_to_next_class(self):
        self.current_class += 1
        return self.current_class

class Teacher(Person):
    def __init__(self, name, surname, age, gender, salary):
        super().__init__(self,name, surname, age, gender)
        self._salary = salary
        
    def increase_salary(self, increasing):
        self.salary = self.salary + self.increasing
        return self.current_class


    def get_salary(self):
        ...