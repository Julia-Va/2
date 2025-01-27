class Library:
    def __init__(self, books=None):
        # Инициализируем атрибут books, если не передан, создаем пустой список
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        """Возвращает идентификатор для добавления новой книги."""
        if not self.books:  # Если список книг пустой,
            return 1       # возвращаем 1
        else:
            # Возвращаем id последней книги (+1)
            return max(book['id'] for book in self.books) + 1

    def get_index_by_book_id(self, book_id):
        """Возвращает индекс книги по её идентификатору."""
        for index, book in enumerate(self.books):
            if book['id'] == book_id:
                return index
        # Если не нашли книгу с таким id, вызываем ошибку ValueError
        raise ValueError("Книги с запрашиваемым id не существует")