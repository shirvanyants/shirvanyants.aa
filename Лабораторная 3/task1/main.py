class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise TypeError("Author must be a string")
        self._author = value

    def __str__(self):
        return f"{self.name} by {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.author})"


class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Pages must be an integer")
        if value <= 0:
            raise ValueError("Pages must be a positive integer")
        self._pages = value

    def __str__(self):
        return f"{self.name} by {self.author}, {self.pages} pages"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.author}, {self.pages})"


class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise TypeError("Duration must be a float")
        if value <= 0:
            raise ValueError("Duration must be a positive float")
        self._duration = value

    def __str__(self):
        return f"{self.name} by {self.author}, {self.duration} hours"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.author}, {self.duration})"


if __name__ == "__main__":
    book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
    paper_book = PaperBook("The Lord of the Rings", "J.R.R. Tolkien", 1207)
    audio_book = AudioBook("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 8.7)

    print(book)
    print(paper_book)
    print(audio_book)
