class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = None
        self.set_name = name
        self._author = None
        self.set_author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс книги. """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if isinstance(pages, int):
            if pages > 0:
                self.pages = pages
            else:
                raise AttributeError(f'Error input count of pages: {pages!r}')
        else:
            raise AttributeError(f'Error input type of pages: {pages!r}')

    def __str__(self):
        return f"Книга: {self.name}\nАвтор: {self.author}\nСтраниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Длительность должна быть типа float")
        if duration <= 0:
            raise ValueError("Длительность должна быть положительным числом")

        self._duration = None
        self.set_duration = duration

    @property
    def duration(self):
        return self._duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"
