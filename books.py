# books.py - базовый класс для книг

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_info(self):
        return f"Название: {self.title}, Автор: {self.author}"

class Library:
    def __init__(self):
        self.books = []  # Здесь будут храниться все книги
    
    def add_book(self, book):
        """Добавляет книгу в библиотеку"""
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в библиотеку")
    
    def find_books_by_author(self, author):
        """Ищет книги по автору"""
        found_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                found_books.append(book)
        return found_books
    
    def get_all_books(self):
        """Возвращает все книги"""
        return self.books
    
    def display_all_books(self):
        """Показывает все книги в библиотеке"""
        if not self.books:
            print("Библиотека пуста")
        else:
            print("=== КНИГИ В БИБЛИОТЕКЕ ===")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book.get_info()}")