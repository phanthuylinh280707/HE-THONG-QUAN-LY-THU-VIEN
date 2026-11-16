import pytest
from unittest.mock import Mock

from src.services.book_service import (
    BookService,
    BookAlreadyExistsError
)


# Tạo dữ liệu sách giả lập
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author


# Khởi tạo dữ liệu trước mỗi test
@pytest.fixture
def setup_service():
    mock_repository = Mock()
    service = BookService(mock_repository)

    return service, mock_repository


# TEST 1: Thêm sách thành công
def test_add_book_success(setup_service):
    service, repository = setup_service

    book = Book("B001", "Lap trinh Python", "Nguyen Van A")

    repository.find_by_id.return_value = None

    result = service.addBook(book)

    assert result is True

    repository.save.assert_called_once_with(book)


# TEST 2: Thêm sách bị trùng mã
def test_add_book_duplicate(setup_service):
    service, repository = setup_service

    book = Book("B001", "Lap trinh Python", "Nguyen Van A")

    repository.find_by_id.return_value = book

    with pytest.raises(BookAlreadyExistsError):
        service.addBook(book)

    repository.save.assert_not_called()


# TEST 3: Thiếu mã sách
def test_add_book_empty_id(setup_service):
    service, repository = setup_service

    book = Book("", "Lap trinh Python", "Nguyen Van A")

    with pytest.raises(ValueError):
        service.addBook(book)

    repository.save.assert_not_called()


# TEST 4: Thiếu tên sách
def test_add_book_empty_title(setup_service):
    service, repository = setup_service

    book = Book("B001", "", "Nguyen Van A")

    with pytest.raises(ValueError):
        service.addBook(book)

    repository.save.assert_not_called()


# TEST 5: Thiếu tên tác giả
def test_add_book_empty_author(setup_service):
    service, repository = setup_service

    book = Book("B001", "Lap trinh Python", "")

    with pytest.raises(ValueError):
        service.addBook(book)

    repository.save.assert_not_called()


# TEST 6: Kiểm tra Repository được gọi đúng một lần
def test_repository_save_called_once(setup_service):
    service, repository = setup_service

    book = Book("B002", "Co so du lieu", "Tran Van B")

    repository.find_by_id.return_value = None

    service.addBook(book)

    repository.save.assert_called_once()