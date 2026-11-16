
class BookService:
    def __init__(self, book_repository):
        self.book_repository = book_repository

    # Them sach va kiem tra logic
    def addBook(self, book):

        # 1. Kiem tra ma sach
        if not isinstance(book.book_id, str) or not book.book_id.strip():
            return False, "Ma sach khong duoc de trong!"

        # 2. Kiem tra ten sach
        if not isinstance(book.title, str) or not book.title.strip():
            return False, "Ten sach khong duoc de trong!"

        # 3. Kiem tra tac gia
        if not isinstance(book.author, str) or not book.author.strip():
            return False, "Ten tac gia khong duoc de trong!"

        # 4. Kiem tra nam xuat ban
        if not isinstance(book.year, int) or isinstance(book.year, bool):
            return False, "Nam xuat ban phai la so nguyen!"

        if book.year <= 0:
            return False, "Nam xuat ban khong hop le!"

        # 5. Kiem tra ma sach trung lap
        for existing_book in self.book_repository.get_all_books():
            if existing_book.book_id.strip().lower() == book.book_id.strip().lower():
                return False, "Ma sach da ton tai!"

        # 6. Them sach neu du lieu hop le
        book.book_id = book.book_id.strip()
        book.title = book.title.strip()
        book.author = book.author.strip()

        self.book_repository.add_book(book)

        return True, "Them sach thanh cong!"
