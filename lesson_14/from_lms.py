class Animal:
    def say_hi(self):
        pass


class Cat(Animal):
    def say_hi(self):
        return 'meow'


class Dog(Animal):
    def say_hi(self):
        return 'bow'


def animals_say_hello(animal):
    print(animal.say_hi())


# def animal_say_hello(animal):
#     print(animal.say_hi)

cat = Cat()
dog = Dog()

animals_say_hello(cat)
animals_say_hello(dog)