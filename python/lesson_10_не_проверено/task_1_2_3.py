class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow_book(self):
        self.is_borrowed = True

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False

    def get_status(self):
        if self.is_borrowed:
            print('Взята')
        else:
            print('Доступна')


book_data = Book('Война и мир', 'Лев Толстой')
book_data.get_status() # Доступна

book_data.borrow_book()
book_data.get_status()  # Взята

book_data.return_book()
book_data.get_status()  # Доступна
