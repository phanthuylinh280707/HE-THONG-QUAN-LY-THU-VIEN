
public class BookUpdateService {

    // Lớp lưu trữ thông tin sách
    static class Book {
        private String bookId;
        private String bookName;
        private String author;
        private int quantity;

        public Book(String bookId, String bookName,
                    String author, int quantity) {
            this.bookId = bookId;
            this.bookName = bookName;
            this.author = author;
            this.quantity = quantity;
        }

        public void displayInfo() {
            System.out.println("Ma sach: " + bookId);
            System.out.println("Ten sach: " + bookName);
            System.out.println("Tac gia: " + author);
            System.out.println("So luong: " + quantity);
        }
    }

    // Chuc nang cap nhat thong tin sach
    public boolean updateBook(Book book, String newName,
                              String newAuthor, int newQuantity) {

        if (book == null || newName == null ||
            newAuthor == null || newName.trim().isEmpty() ||
            newAuthor.trim().isEmpty() || newQuantity < 0) {
            System.out.println("Thong tin cap nhat khong hop le!");
            return false;
        }

        book.bookName = newName;
        book.author = newAuthor;
        book.quantity = newQuantity;

        System.out.println("Cap nhat thong tin sach thanh cong!");
        return true;
    }

    public static void main(String[] args) {

        BookUpdateService service = new BookUpdateService();

        Book book = new Book("S001", "Lap trinh Java",
                            "Nguyen Van A", 10);

        System.out.println("THONG TIN SACH BAN DAU:");
        book.displayInfo();

        System.out.println("\nTHUC HIEN CAP NHAT:");

        service.updateBook(book, "Lap trinh Java nang cao",
                           "Tran Van B", 15);

        System.out.println("\nTHONG TIN SACH SAU KHI CAP NHAT:");
        book.displayInfo();
    }
}
