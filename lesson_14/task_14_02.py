# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []

class Author:

    def __init__(self, name: object, country: object, birthday: object, books: list) -> object:
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = books
    def __repr__(self):
        return f'author - {self.name}, country - {self.country}, birthday - {self.birthday}, books - {self.books}'
    def __str__(self):
        return f'author - {self.name}, country - {self.country}, birthday - {self.birthday}, books - {self.books}'


class Book:

    amount_of_books = 0

    def __init__(self, name, year, author):
        self.title = name
        self.year = year
        self.author = author
        Book.amount_of_books +=1

    def __repr__(self):
        return f'title - {self.title}, year - {self.year}, author - {self.author.name}'

    def __str__(self):
        return f'title - {self.title}, year - {self.year}, author - {self.author.name}'

# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year

class Library:

    def __init__(self, books: list, authors: list):
        self.books = books
        self.authors = authors

    def __repr__(self):
        return f'books - {self.books}, authors - {self.authors}'

    def __str__(self):
        return f'books - {self.books}, authors - {self.authors}'

    def new_book(self, ):


    def group_by_author(self):

    def group_by_year(self):


author = Author('franko', 'ukraine', 1812, ['book1', 'book2', 'book3'])
print(author)
this_book = Book('house', 1854, author)
print(Book.amount_of_books)