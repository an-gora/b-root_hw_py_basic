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


# for movie, movieinfo in list_of_media.items():
#     print({movie})
#     title = movieinfo['title']
#     year = movieinfo['year']
#     print(f'инфо про фильм {movie}: название {title}, выпущен в {year} году')


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
            break
        else:
            print(f'hhhmmmm...seems here is no movie with name {movie}')


filter_by_name()