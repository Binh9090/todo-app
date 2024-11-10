import tkinter as tk
from tkinter import messagebox

# Tạo ứng dụng và cài đặt kích thước
app = tk.Tk()
app.title("To-do List Siêu Đơn Giản 🍉")
app.geometry("400x300")

# Hàm thêm nhiệm vụ vào danh sách
def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Ơ kìa!", "Hãy nhập gì đó đi bạn ơi!")

# Hàm xóa nhiệm vụ đã chọn
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Ơ kìa!", "Hãy chọn nhiệm vụ cần xóa nha!")

# Tạo ô nhập liệu
entry = tk.Entry(app, width=30)
entry.pack(pady=10)

# Tạo nút Thêm
add_button = tk.Button(app, text="Thêm nhiệm vụ", command=add_task)
add_button.pack(pady=5)

# Tạo danh sách nhiệm vụ
listbox = tk.Listbox(app, width=50, height=10)
listbox.pack(pady=10)

# Tạo nút Xóa
delete_button = tk.Button(app, text="Xóa nhiệm vụ", command=delete_task)
delete_button.pack(pady=5)

# Khởi động ứng dụng
app.mainloop()
