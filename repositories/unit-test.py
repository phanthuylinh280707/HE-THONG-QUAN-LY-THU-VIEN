
import pytest
from unittest.mock import Mock

from services.book_service import BookService


# Tao du lieu sach gia lap
class Book:
    def __init__(self, book_id, title, author, year=2024):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year


# Khoi tao Service truoc moi test
@pytest.fixture
def setup_service():
    mock_repository = Mock()
    mock_repository.get_all_books.return_value = []

    service = BookService(mock_repository)

    return service, mock_repository


# TEST 1: Them sach thanh cong
def test_add_book_success(setup_service):
    service, repository = setup_service

    book = Book("B001", "Lap trinh Python", "Nguyen Van A")

    result = service.addBook(book)

    assert result[0] is True
    assert result[1] == "Them sach thanh cong!"

    repository.add_book.assert_called_once_with(book)


# TEST 2: Them sach bi trung ma
def test_add_book_duplicate(setup_service):
    service, repository = setup_service

    book = Book("B001", "Lap trinh Python", "Nguyen Van A")

    repository.get_all_books.return_value = [book]

    result = service.addBook(book)

    assert result[0] is False
    assert result[1] == "Ma sach da ton tai!"

    repository.add_book.assert_not_called()


# TEST 3: Thieu ma sach
def test_add_book_empty_id(setup_service):
    service, repository = setup_service

    book = Book("", "Lap trinh Python", "Nguyen Van A")

    result = service.addBook(book)

    assert result[0] is False
    repository.add_book.assert_not_called()


# TEST 4: Thieu ten sach
def test_add_book_empty_title(setup_service):
    service, repository = setup_service

    book = Book("B001", "", "Nguyen Van A")

    result = service.addBook(book)

    assert result[0] is False
    repository.add_book.assert_not_called()


# TEST 5: Thieu ten tac gia
def test_add_book_empty_author(setup_service):
    service, repository = setup_service

    book = Book("B001", "Lap trinh Python", "")

    result = service.addBook(book)

    assert result[0] is False
    repository.add_book.assert_not_called()


# TEST 6: Nam xuat ban khong hop le
def test_add_book_invalid_year(setup_service):
    service, repository = setup_service

    book = Book("B002", "Co so du lieu", "Tran Van B", -2024)

    result = service.addBook(book)

    assert result[0] is False
    assert result[1] == "Nam xuat ban khong hop le!"

    repository.add_book.assert_not_called()
