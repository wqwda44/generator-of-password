import string
import random
import keyboard
import tkinter as tk
from tkinter import messagebox
import pyperclip

# Генерация пароля
def pasgen(length, use_letters=True, use_digits=True, use_punctuation=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        raise ValueError("No characters selected for password generation")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Функция для генерации и отображения паролей
def generate_passwords():
    length = int(entry_length.get())
    if length < 1:
        messagebox.showerror("Error", "Password length should be at least 1")
        return

    use_letters = var_letters.get()
    use_digits = var_digits.get()
    use_punctuation = var_punctuation.get()

    num_passwords = int(entry_num_passwords.get())
    passwords = [pasgen(length, use_letters, use_digits, use_punctuation) for _ in range(num_passwords)]

    with open('generated.txt', 'w', encoding='utf-8') as file:
        for i, password in enumerate(passwords):
            label = f"Password {i+1}"
            file.write(f"{label}: {password}\n")

    messagebox.showinfo("Success", "Passwords generated and saved to 'generated.txt'")

    # Отображение паролей в текстовом поле
    text_passwords.delete("1.0", tk.END)
    for password in passwords:
        text_passwords.insert(tk.END, f"{password}\n")
    
    # Копирование последнего пароля в буфер обмена
    pyperclip.copy(passwords[-1])
    messagebox.showinfo("Copied", "Last generated password copied to clipboard")

# Создание GUI
root = tk.Tk()
root.title("Password Generator")

# Поля ввода и метки
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Number of Passwords:").grid(row=1, column=0, padx=10, pady=10)
entry_num_passwords = tk.Entry(root)
entry_num_passwords.grid(row=1, column=1, padx=10, pady=10)

# Флажки для выбора символов
var_letters = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_punctuation = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=var_letters).grid(row=2, column=0, padx=10, pady=5)
tk.Checkbutton(root, text="Include Digits", variable=var_digits).grid(row=2, column=1, padx=10, pady=5)
tk.Checkbutton(root, text="Include Punctuation", variable=var_punctuation).grid(row=2, column=2, padx=10, pady=5)

# Кнопка для генерации паролей
btn_generate = tk.Button(root, text="Generate Passwords", command=generate_passwords)
btn_generate.grid(row=3, column=0, columnspan=3, pady=20)

# Текстовое поле для отображения паролей
text_passwords = tk.Text(root, height=10, width=50)
text_passwords.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
