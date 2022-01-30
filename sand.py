# class Car:
#     amount_of_instances = 0
#
#     def __init__(self, color):
#         self.color = color
#         Car.amount_of_instances +=1
#
# car_1 = Car('green')
# car_2 = Car('blue')
# print(Car.amount_of_instances)


# Действительно, super() может быть использована вне класса. Пример:
#
# d = Discount()
# print(super(Discount, d).price())

# class O:
#     def method(self):
#         print('I am O')
# class A(O):
#     def method(self):
#         super().method()
#         print('I am A')
# class B(O):
#     def method(self):
#         super().method()
#         print('I am B')
# class C(A, B):
#     def method(self):
#         super().method()
#         print('I am C')
# C().method()

a = float(0)
print(a)


def filter_by_name():
    mymovie = input('what movie are you looking for? ')
    for movie, movieinfo in list_of_media.items():
        if movieinfo['title'] == mymovie:
            year = movieinfo['year']
            genre = movieinfo['genre']
            rating = movieinfo['rating']
            print(f'Here is info about movie {mymovie}: \n'
                  f'released at {year}\n'
                  f'genre is {genre}\n'
                  f'rating is {rating}')

def filter_by_name():
    movie = input('what movie are you looking for? ')
    has_such_movie = []
    for k_1 in list_of_media.keys():
        mydict = list_of_media[k_1]
        if ([v for k, v in mydict.items() if k == 'title' and v == movie]):
            has_such_movie.append(mydict)
        else:
            continue
    if has_such_movie:
        print(f'here is info about {movie} movie: \n {mydict}')
    else:
        print(f'hhhmmmm...seems here is no movie with name {movie}')
