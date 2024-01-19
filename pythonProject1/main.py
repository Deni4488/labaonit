import sqlite3
import tkinter as tk
from tkinter import messagebox

# Создаем соединение с базой данных
conn = sqlite3.connect('newdb.db')
c = conn.cursor()

# Создаем таблицу students
c.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)")

# Функция для добавления студента
def add_student():
    name = entry_name.get()
    print(name)
    age = entry_age.get()
    c.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    messagebox.showinfo("Успех", "Студент успешно добавлен")

# Функция для удаления студента
def delete_student():
    id = entry_id.get()
    c.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    messagebox.showinfo("Успех", "Студент успешно удален")

# Функция для обновления возраста студента
def update_age():
    id = entry_id.get()
    age = entry_age.get()
    c.execute("UPDATE students SET age = ? WHERE id = ?", (age, id))
    conn.commit()
    messagebox.showinfo("Успех", "Возраст студента успешно обновлен")

# Создаем окно
window = tk.Tk()
window.geometry("800x600")
window.title("Управление базой данных")

# Добавляем поля ввода
# Добавляем поле ввода и метку
entry_name = tk.Entry(window)
entry_name.pack()

label_name = tk.Label(window, text="Введите имя студента:")
label_name.pack()

# Обновляем текст метки каждый раз, когда пользователь вводит что-то в поле ввода
# entry_name.bind('<Insert>', lambda e: label_name.config(text="Введите ваше имя: " + entry_name.get()))
entry_age = tk.Entry(window)
entry_age.pack()

label_age = tk.Label(window, text="Введите возраст студента:")
label_age.pack()

entry_id = tk.Entry(window)
entry_id.pack()
label_id = tk.Label(window, text="Введите id студента, которого хотите удалить:")
label_id.pack()
# Добавляем кнопки
button_add = tk.Button(window, text="Добавить", command=add_student)
button_add.pack()

button_delete = tk.Button(window, text="Удалить", command=delete_student)
button_delete.pack()

button_update = tk.Button(window, text="Обновить", command=update_age)
button_update.pack()

# Запускаем главный цикл обработки событий
window.mainloop()

# Закрываем соединение с базой данных
conn.close()
