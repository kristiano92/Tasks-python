class Library:
    def __init__(self, title, author, year, number_of_pages, press, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.number_of_pages = number_of_pages
        self.press = press
        self.isbn = isbn

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

b1 = Library("W pustyni i w puszczy", "Henryk Sienkiewicz", 1989, 200, "PWN", 1234567891)
print(b1)
