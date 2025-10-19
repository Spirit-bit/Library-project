# books.py - базовый класс для книг

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_info(self):
        return f"Название: {self.title}, Автор: {self.author}"