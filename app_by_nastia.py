from typing import Dict

list_of_media: dict[str, dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]] = {
    'movie_id_1': {'title': 'Mask', 'year': '2001', 'genre': 'comedy', 'rating': 0},
    'movie_id_2': {'title': 'Titanic', 'year': '1996', 'genre': 'drama', 'rating': 0},
    'movie_id_3': {'title': 'Screem', 'year': '2003', 'genre': 'horror', 'rating': 0},
    'movie_id_4': {'title': 'Matrix', 'year': '2003', 'genre': 'action', 'rating': 0},
}

list_of_users = {
    'user_1': 'tom',
    'user_2': 'mary',
    'user_3': 'bob',
}

movies_and_users = {
    'user_1': {'watched_movies': ['movie_id_1', 'movie_id_2', 'movie_id_3'],
               'favourite': ['movie_id_1', 'movie_id_1'],
               'liked_movies': ['movie_id_1', 'movie_id_2'],
               'planed_to_watch': ['movie_id_4']
               },
    'user_2': {'watched_movies': ['movie_id_2', 'movie_id_3', 'movie_id_4'],
               'favourite': ['movie_id_4'],
               'liked_movies': ['movie_id_4'],
               'planed_to_watch': ['movie_id_1']
               },
    'user_3': {'watched_movies': ['movie_id_2', 'movie_id_3', 'movie_id_4'],
               'favourite': ['movie_id_4'],
               'liked_movies': ['movie_id_2'],
               'planed_to_watch': ['movie_id_1']
               }
}


def looking_for():
    user = input('whom are you looking for?: ')
    return user


def is_member(name):
    return name in list_of_users.values()


def get_user_id(name):
    user_key = ''.join([k for k, v in list_of_users.items() if v == name])
    return (user_key)


def choose(user_id):
    action = input('Choose what you want to see: all, liked or fav movie list: ')
    if action == 'all':
        # красиво вывести только все titles
        return list_of_media
    elif action == 'fav':
        # ошибка если в списке больше чем 1 фильм
        return list_of_media[''.join(movies_and_users[user_id]['favourite'])]['title']
    elif action == 'liked':
        # #ошибка если в списке больше чем 1 фильм
        return list_of_media[''.join(movies_and_users[user_id]['liked_movies'])]['title']


def filter_by_year():
    year = input('movie released at ')
    has_such_year = []
    for k_1 in list_of_media.keys():
        mydict = list_of_media[k_1]
        if ([v for k, v in mydict.items() if k != 'title' and v == year]):
            has_such_year.append(mydict['title'])
        else:
            continue
    if has_such_year:
        print(f"Here is list of movies in your media released at {year}: {has_such_year}")
    else:
        print(f'hhhmmmm...seems here is no movie in your media released at {year}')


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


def filter_by_genre():
    genre = input('What genre are you looking for? Comedy, drama, horror or action?: ')
    has_such_genre = []
    for k_1 in list_of_media.keys():
        mydict = list_of_media[k_1]
        if ([v for k, v in mydict.items() if k != 'title' and v == genre]):
            has_such_genre.append(mydict['title'])
        else:
            continue
    if has_such_genre:
        print(f"Here is list of {genre} movies in your media: {has_such_genre}")
    else:
        print(f'hhhmmmm...seems here is no such genre in your media  ')


def choose_next_step(name):
    next_step = input('Do you want to continue (y/n): ')
    if next_step == 'n':
        print(f'Bye bye, {name}! Hope to see you soon!')
        exit()
    elif next_step == 'y':
        print(f'Lets find some movie, {name}')
    else:
        choose_next_step(name)



def main():
    name = looking_for()
    if is_member(name):
        user_id = get_user_id(name)
    else:
        print('hhhmm...seems there is no such person in that family')
        exit()
    # print(choose(user_id))
    # filter_by_genre()
    # choose_next_step(name)
    # filter_by_name()
    choose_next_step(name)


if __name__ == '__main__':
    main()