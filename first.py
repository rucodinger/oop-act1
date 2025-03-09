from module import search

class Library:
    def __init__(self):
        self.books = []

    def find_book(self, name):
        results = search(name, self.books)[0]
        if len(results) > 0:
            print(f"Найдено книг: {len(results)}")
            for result in results:
                val = f"\n{'-' * 5}{result.name}{'-' * 5}\nАвтор: {result.author}\nГод написания: {result.year}\n"
                if result.is_available:
                    val += "Книга доступна"
                elif not result.is_in_library:
                    val += "Книга отсутствует"
                else: val += "Книга взята"
                val += "\n"
                val += "-" * (len(result.name) + 10)
                print(val)
        else:
            print("Книг с таким названием не найдено\n")

    def add_book(self, book):
        if not book.is_in_library:
            book.is_in_library = True
            self.books.append(book)

    def remove_book(self, name):
        books, indices = search(name, self.books)[0], search(name, self.books)[1]
        if len(books) == 0:
            print("Книг с таким названием не найдено\n")
        else:
            for i in sorted(indices, reverse=True):
                del self.books[i]

    def borrow_book(self, name):
        books, indices = search(name, self.books)[0], search(name, self.books)[1]
        if len(books) > 0:
            book = books[0]
            if book.is_available:
                self.books[indices[0]].is_available = False
                print(f"Вы успешно взяли книгу {book.name}\n")

    def return_book(self, name):
        books, indices = search(name, self.books)[0], search(name, self.books)[1]
        if len(books) > 0:
            book = books[0]
            if book.borrowed:
                self.books[indices[0]].is_available = True
                print(f"Вы успешно вернули книгу {book.name}\n")

class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
        self.is_available = True
        self.is_in_library = False


lib = Library()
book = Book("Book", "Author", 1999)
book1 = Book("Book1", "er", 1876)
lib.add_book(book)
lib.add_book(book1)
lib.find_book("Book")
lib.borrow_book("Book")
lib.find_book("Book")