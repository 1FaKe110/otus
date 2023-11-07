class Book:

    def __init__(self, Title, Author, Genre, Pages, Publisher, **kwargs):
        self.title = Title
        self.author = Author if Author != '' else "Не указан"
        self.genre = Genre
        self.pages = Pages
        self.publisher = Publisher
        self.etc = kwargs

    def __dict__(self):
        return dict(title=self.title,
                    author=self.author,
                    genre=self.genre,
                    pages=self.pages)

    def as_dict(self):
        return self.__dict__()

    def __repr__(self):
        return f'Book[{self.title}]'

    def __str__(self):
        return self
