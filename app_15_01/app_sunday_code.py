import pathlib
import uuid
from typing import TypeAlias, NamedTuple, Any
from pydantic import BaseModel, Field

T_MOVIE_ID: TypeAlias = uuid.UUID
T_USER_ID: TypeAlias = uuid.UUID


class MenuListItem(NamedTuple):
    text: str
    given_object: Any


class User(BaseModel):
    user_id: T_USER_ID
    username: str


class Users(BaseModel):
    __root__: list[User]


class Movie(BaseModel):
    movie_id: T_MOVIE_ID
    title: str
    year: int
    genre: str


class Movies(BaseModel):
    __root__: list[Movie]


class Reaction(BaseModel):
    movie_id: T_MOVIE_ID
    user_id: T_USER_ID
    like: bool = Field(default=False)
    watched: bool = Field(default=False)
    planned: bool = Field(default=False)


class Reactions(BaseModel):
    __root__: list[Reaction]


class DataApi():
    __path_to_project = pathlib.Path(__file__).parent
    __path_to_users = __path_to_project.joinpath('users.json')
    __path_to_movies = __path_to_project.joinpath('movies.json')
    __path_to_reactions = __path_to_project.joinpath('reactions.json')

    def get_from_file(self, db_file):
        return Users.parse_file(db_file).__root__

    def get_users_list(self):
        raw_list = self.get_from_file(self.__path_to_users)
        output = []
        for item in raw_list:
            output.append(MenuListItem(text=item.username, given_object=item))
        return output

    def get_movie_list(self):
        raw_list = self.get_from_file(self.__path_to_movies)
        output = []
        for item in raw_list:
            output.append(MenuListItem(text=f'{item.title} {item.year} {item.genre}', given_object=item))
        return output


class View:
    def view_list(self, list):
        for index, item in enumerate(list, 1):
            print(f'{index}. {item.text}')


class App:
    data_api = DataApi()
    new_view = View()
    selected_user = None

    def choose_user(self):
        user_list = self.data_api.get_users_list()
        self.new_view.view_list(user_list)

        while self.selected_user == None:
            answer = self.message('Choose the user by number: ')
            try:
                self.selected_user = user_list[int(answer) - 1].given_object.user_id
            except IndexError:
                print('Wrong value -- choose correct number')
            except ValueError:
                print('Wrong value')
        return self.selected_user

    def message(self, question):
        return input(question)

    def menu(self):
        selected_option = input('''Choose an option:
        1. All movies
        2. Filter movies
        3. Choose the movie
        ''')

        if selected_option == 1:
            self.all_movies()

    def all_movies(self):
        movies_list = self.data_api.get_movie_list()
        self.new_view.view_list(movies_list)


class Media:

    def __init__(self, movie, reaction):
        self.movie = movie
        self.reaction = reaction

    def __str__(self):
        return f'{self.movie.name} {self.reaction.like}'


def main():
    # __path_to_project = pathlib.Path(__file__).parent
    # __path_to_movies = __path_to_project.joinpath('movies.json')
    # test_movies = Movies(__root__=[
    #     Movie(movie_id=uuid.uuid4(), title='scream', year = 2000, genre = 'horror'),
    #     Movie(movie_id=uuid.uuid4(), title='mask', year = 2001, genre = 'comedy'),
    #     Movie(movie_id=uuid.uuid4(), title='batman', year=2005, genre = 'action')
    # ])
    # print(*test_movies, sep='\n')
    # raw_json_movies = test_movies.json(indent=2)
    # __path_to_movies.write_text(raw_json_movies)
    # ...
    # __path_to_project = pathlib.Path(__file__).parent
    # __path_to_users = __path_to_project.joinpath('users.json')
    # test_users = Users(__root__=[
    #     User(user_id=uuid.uuid4(),username='tom'),
    #     User(user_id=uuid.uuid4(), username='sam')
    # ])
    # # print(*test_users,sep='\n')
    # raw_json = test_users.json(indent=2)
    #
    #
    # __path_to_users.write_text(raw_json)
    #
    # data_api = DataApi()
    # us_list = data_api.get_users_list()
    # print(us_list)

    app = App()
    app.choose_user()
    app.menu()


if __name__ == '__main__':
    main()

"""
    def get_records(cls, search=None):
        # if search != None:

        output = {}
        for index, record in enumerate(cls.pbook_2, 1):
            output[index] = MenuItem(
                text=f'{record.full_name():25}{str(record.telephone):10}{record.city}',
                action=cls.select_record,
                action_args=record
            )
        cls.draw_list(output)
        cls.choise_menu(output)




    def choise_menu(cls, menu):
        try:
            key_input = int(input('Enter an option: '))
        except ValueError:
            print('Input invalid')
            cls.choise_menu(menu)
        try:
            menu[key_input].action(menu[key_input].action_args)
        except KeyError:
            print('Input invalid')
            cls.choise_menu(menu)
