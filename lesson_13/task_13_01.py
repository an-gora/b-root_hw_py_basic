# Make a class structure in python representing people at school.
# Make a base class called Person, a class called Student,
# and another one called Teacher. Try to find as many methods and
# attributes as you can which belong to different classes,
# and keep in mind which are common and which are not.
# For example, the name should be a Person attribute,
# while salary should only be available to the teacher.

class Person:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender


class Student(Person):
    def __init__(self, name, surname, age: int, gender, current_class: int):
        super().__init__(name, surname, age, gender)
        self.current_class = current_class

    def go_to_next_class(self):
        self.current_class += 1
        return self.current_class

    def is_graduation(self):
        if self.current_class == 11:
            return 'Congs! This student is graduated!'
        else:
            return 'Not yet'


class Teacher(Person):
    def __init__(self, name, surname, age, gender, salary):
        super().__init__(name, surname, age, gender)
        self.__salary = salary

    def increase_salary(self, increasing):
        self.salary = self.salary + self.increasing
        return self.current_class

    def get_salary(self):
        return self.__salary


bob = Student('Bob', 'Brown', 12, 'male', 7)
print(bob.is_graduation())

mary = Teacher('Marry', 'Wolf', 35, 'female', 1000)
print(mary.get_salary())

