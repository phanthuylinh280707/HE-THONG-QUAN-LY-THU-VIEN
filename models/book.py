class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print("Mã sách:", self.book_id)
        print("Tên sách:", self.title)
        print("Tác giả:", self.author)
        print("Năm xuất bản:", self.year)
