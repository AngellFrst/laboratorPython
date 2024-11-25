import random
import os
import tkinter as tk
from tkinter import filedialog

folder_path = "C:/Users/error/Desktop/borisov"

def create_file(filename):
    with open(os.path.join(folder_path, filename), 'w') as file:
        for _ in range(10):
            number = random.randint(1, 10)
            file.write(f"{number}\n")
    print(f"Файл '{filename}' создан с случайными числами.")

def read_file(filepath):
    with open(filepath, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    print("Содержимое файла:", numbers)
    average = sum(numbers) / len(numbers)
    print(f"Среднее значение чисел: {average}")

def select_file():
    root = tk.Tk()
    root.withdraw()
    filepath = filedialog.askopenfilename(initialdir=folder_path, title="Выберите файл",
                                          filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if filepath:
        print(f"Вы выбрали файл: {filepath}")
        read_file(filepath)
    else:
        print("Файл не выбран.")

create_file("file1.txt")
create_file("file2.txt")
select_file()

