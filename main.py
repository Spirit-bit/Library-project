# main.py - тестируем нашу библиотеку

from books import Book, Library

# Создаем библиотеку
my_library = Library()

# Создаем несколько книг
book1 = Book("Гарри Поттер", "Джоан Роулинг")
book2 = Book("Властелин Колец", "Джон Толкин")
book3 = Book("Хоббит", "Джон Толкин")

# Добавляем книги в библиотеку
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# Показываем все книги
my_library.display_all_books()

# Ищем книги Толкина
print("\n=== ПОИСК КНИГ ТОЛКИНА ===")
tolkin_books = my_library.find_books_by_author("Джон Толкин")
for book in tolkin_books:
    print(f"Найдена: {book.get_info()}")