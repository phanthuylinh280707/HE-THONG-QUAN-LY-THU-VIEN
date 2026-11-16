class BookRepository:
    def __init__(self):
        self.books = []

    # Thêm sách
    def add_book(self, book):
        self.books.append(book)

    # Lấy danh sách sách
    def get_all_books(self):
        return self.books

    # Tìm sách theo mã
    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    # Xóa sách
    def delete_book(self, book_id):
        book = self.find_book(book_id)
        if book:
            self.books.remove(book)
            return True
        return False
