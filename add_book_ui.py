
import tkinter as tk
from tkinter import messagebox


# Tạo cửa sổ chính
root = tk.Tk()
root.title("HỆ THỐNG QUẢN LÝ THƯ VIỆN")
root.geometry("600x500")
root.configure(bg="#EAF2F8")
root.resizable(False, False)


# Tiêu đề
title_label = tk.Label(
    root,
    text="THÊM SÁCH MỚI",
    font=("Arial", 22, "bold"),
    fg="#1F4E79",
    bg="#EAF2F8"
)
title_label.pack(pady=25)


# Khung nhập thông tin
form = tk.Frame(root, bg="white", padx=35, pady=25)
form.pack(padx=35, fill="both")


# Hàm tạo ô nhập
def create_input(label_text, row):
    label = tk.Label(
        form,
        text=label_text,
        font=("Arial", 12),
        bg="white"
    )
    label.grid(row=row, column=0, sticky="w", pady=12)

    entry = tk.Entry(
        form,
        font=("Arial", 12),
        width=35
    )
    entry.grid(row=row, column=1, pady=12, padx=10)

    return entry


# Các trường thông tin sách
entry_title = create_input("Tên sách:", 0)
entry_author = create_input("Tác giả:", 1)
entry_isbn = create_input("Mã ISBN:", 2)


# Hàm thêm sách
def add_book():
    book_title = entry_title.get().strip()
    author = entry_author.get().strip()
    isbn = entry_isbn.get().strip()

    if not book_title or not author or not isbn:
        messagebox.showwarning(
            "Thông báo",
            "Vui lòng nhập đầy đủ thông tin sách!"
        )
        return

    messagebox.showinfo(
        "Thành công",
        f"Thông tin sách đã được nhập:\n"
        f"Tên sách: {book_title}\n"
        f"Tác giả: {author}\n"
        f"ISBN: {isbn}"
    )

    clear_form()


# Hàm làm mới biểu mẫu
def clear_form():
    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_isbn.delete(0, tk.END)
    entry_title.focus()


# Khung chứa nút
button_frame = tk.Frame(root, bg="#EAF2F8")
button_frame.pack(pady=25)


# Nút thêm sách
add_button = tk.Button(
    button_frame,
    text="THÊM SÁCH",
    font=("Arial", 12, "bold"),
    bg="#2874A6",
    fg="white",
    width=15,
    command=add_book
)
add_button.grid(row=0, column=0, padx=10)


# Nút làm mới
clear_button = tk.Button(
    button_frame,
    text="LÀM MỚI",
    font=("Arial", 12, "bold"),
    bg="#85929E",
    fg="white",
    width=15,
    command=clear_form
)
clear_button.grid(row=0, column=1, padx=10)


# Chạy chương trình
root.mainloop()
