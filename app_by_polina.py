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
               'favourite': ['movie_id_1', 'movie_id_2'],
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


def choose(user_id: str) -> None:
    try:
        action = input('Choose what you want to watch:\n'
                       'a = all,\n'
                       'f = favourites,\n'
                       'l = liked movies,\n'
                       'p = planed to watch,\n'
                       'act = act:\n')
        if action == 'a':
            # красиво вывести только все titles
            return all_movies()
        elif action == 'f':
            # ошибка если в списке больше чем 1 фильм
            return fav_movies(user_id)
        elif action == 'l':
            # #ошибка если в списке больше чем 1 фильм
            return liked_movies(user_id)
        elif action == 'p':
            return planed_movies(user_id)
        elif action == 'act':
            return actions_to_movie(user_id)
    except Exception as exc:
        print(exc)
        print('Try again')
        pass


def all_movies() -> list[str]:
    movie_dict = []
    for k in list_of_media.keys():
        temp_dict = list_of_media[k]
        movie_dict.append(temp_dict['title'])
    print(movie_dict)
    return movie_dict


def fav_movies(user_id: str) -> list[str]:
    movie_id_list = []
    movie_list = []
    temp_dict = movies_and_users[user_id]
    if (v for k, v in temp_dict.items() if k == 'favourite'):
        for i in temp_dict['favourite']:
            movie_id_list.append(i)
    for i in movie_id_list:
        movie_list.append(list_of_media[i]['title'])
    print(movie_list)
    return movie_list


def liked_movies(user_id: str) -> list[str]:
    movie_id_list = []
    movie_list = []
    temp_dict = movies_and_users[user_id]
    if (v for k, v in temp_dict.items() if k == 'liked_movies'):
        for i in temp_dict['liked_movies']:
            movie_id_list.append(i)
    for i in movie_id_list:
        movie_list.append(list_of_media[i]['title'])
    print(movie_list)
    return movie_list


def planed_movies(user_id: str) -> list[str]:
    movie_id_list = []
    movie_list = []
    temp_dict = movies_and_users[user_id]
    if (v for k, v in temp_dict.items() if k == 'planed_to_watch'):
        for i in temp_dict['planed_to_watch']:
            movie_id_list.append(i)
    for i in movie_id_list:
        movie_list.append(list_of_media[i]['title'])
    print(movie_list)
    return movie_list


def actions_to_movie(user_id: str) -> None:
    movie = input('Choose the movie: ')
    act = input('What you want to do with this movie? ')

    if act == 'fav':
        add_to_favourite(movie, user_id)
    if act == 'watch':
        add_to_watched(movie, user_id)
    if act == 'plan':
        add_to_planed(movie, user_id)
    if act == 'like':
        like_movie(movie, user_id)

    if act == 'not fav':
        del_from_favourite(movie, user_id)
    if act == 'not plan':
        del_from_planed(movie, user_id)
    if act == 'dislike':
        unlike_movie(movie, user_id)


def get_movie_id(movie: str) -> list[str]:
    movie_id = []
    for i in list_of_media.keys():
        movie_attributes = list_of_media[i]
        if [k for k, v in movie_attributes.items() if v == movie]:
            movie_id = i
            break
    return movie_id


def add_to_watched(movie: str, user_id: str) -> dict[str, str] | str:
    movie_id = get_movie_id(movie)
    if movie_id not in movies_and_users[user_id]['watched_movies']:
        list_of_watched = movies_and_users[user_id]['watched_movies']
        list_of_watched.append(movie_id)
        movies_and_users[user_id].update({'watched_movies': list_of_watched})
        print(f"{movie} is now in your watched movies")

        if movie_id in movies_and_users[user_id]['planed_to_watch']:
            del_from_planed(movie, user_id)
        return movies_and_users[user_id]

    else:
        print("You have already watched this movie")


def add_to_favourite(movie: str, user_id: str) -> dict[str, str] | str:
    movie_id = get_movie_id(movie)
    if movie_id not in movies_and_users[user_id]['favourite']:
        list_of_favourites = movies_and_users[user_id]['favourite']
        list_of_favourites.append(movie_id)
        movies_and_users[user_id].update({'favourite': list_of_favourites})

        print(f"{movie} is in your favourites now")
        return movies_and_users[user_id]

    else:
        print('This movie is already in your favourites')


def add_to_planed(movie: str, user_id: str) -> dict[str, str] | str:
    movie_id = get_movie_id(movie)
    if movie_id not in movies_and_users[user_id]['planed_to_watch']:
        list_of_planed = movies_and_users[user_id]['planed_to_watch']
        list_of_planed.append(movie_id)
        movies_and_users[user_id].update({'planed_to_watch': list_of_planed})

        print(f"{movie} is now in your planed_to_watch movies")
        return movies_and_users[user_id]

    else:
        print("You've already planed to watch this movie")


def like_movie(movie: str, user_id: str) -> dict[str, str] | str:
    movie_id = get_movie_id(movie)
    if movie_id not in movies_and_users[user_id]['liked_movies']:
        list_of_liked = movies_and_users[user_id]['liked_movies']
        list_of_liked.append(movie_id)
        movies_and_users[user_id].update({'liked_movies': list_of_liked})
        print(f"{movie} is now in your liked movies")

        rating = list_of_media[movie_id]['rating'] + 1
        list_of_media[movie_id].update({'rating': rating})
        return movies_and_users[user_id]

    else:
        print("You've already liked this movie")


def del_from_favourite(movie: str, user_id: str) -> dict[str, str] | str:
    movie_id = get_movie_id(movie)
    if movie_id in movies_and_users[user_id]['favourite']:
        list_of_favourites = movies_and_users[user_id]['favourite']
        list_of_favourites.remove(movie_id)
        movies_and_users[user_id].update({'favourite': list_of_favourites})

        print(f"You've removed this movie from favourites")
        return movies_and_users[user_id]

    else:
        print("This movie is not your favourite")


def del_from_planed(movie: str, user_id: str) -> dict[str, str] | str:
    movie_id = get_movie_id(movie)
    if movie_id in movies_and_users[user_id]['planed_to_watch']:
        list_of_planed = movies_and_users[user_id]['planed_to_watch']
        list_of_planed.remove(movie_id)
        movies_and_users[user_id].update({'planed_to_watch': list_of_planed})

        print(f"{movie} removed from your planed_to_watch movies")
        return movies_and_users[user_id]

    else:
        print("You have not planed to watch this movie")


def unlike_movie(movie: str, user_id: str) -> dict[str, str] | str:
    movie_id = get_movie_id(movie)
    if movie_id in movies_and_users[user_id]['liked_movies']:
        list_of_liked = movies_and_users[user_id]['liked_movies']
        list_of_liked.remove(movie_id)
        movies_and_users[user_id].update({'liked_movies': list_of_liked})
        print(f"{movie} removed from your liked movies")

        rating = list_of_media[movie_id]['rating'] - 1
        list_of_media[movie_id].update({'rating': rating})
        return movies_and_users[user_id]

    else:
        print("You haven't liked this movie yet")


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
    while True:
        choose(user_id)
        choose_next_step(name)


if __name__ == '__main__':
    main()