import tkinter as tk
from tkinter import messagebox, filedialog
import random
import os
from PIL import Image
# import ttkbootstrap as ttk

print('Программа открыта')

#кинотеартр

class Kinoteatr:
    def __init__(self, nameFilms, yerFilm=2015, cena=150):
        self.nameFilms = nameFilms  
        self.yerFilm = yerFilm  
        self.cena = cena  

    def filmTiket(self):
        return f"Фильм: {self.nameFilms} / Год: {self.yerFilm} / Цена: {self.cena} рублей"


class Session(Kinoteatr):
    def __init__(self, nameFilms, yerFilm=2015, cena=150, date="7-03-2001", start_time="19:00"):
        super().__init__(nameFilms, yerFilm, cena)
        self.date = date  
        self.start_time = start_time  

    def session_info(self):
        film_info = self.filmTiket()
        return f"Сеанс фильма {self.nameFilms} состоится {self.date} в {self.start_time}.\n{film_info}"


#натройки приложения

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Programms")
        self.geometry("600x400")
        self.name = ""
        self.folder_path = "C:/Users/error/Desktop/borisov" 
        self.configure(bg="#7B68EE")  

       
        self.main_frame = tk.Frame(self, bg="#7B68EE")
        self.main_frame.pack(fill="both", expand=True)

        self.init_name_screen()


#ввод имени
    def init_name_screen(self):

        self.clear_frame()
        label = tk.Label(self.main_frame, text="Как тебя зовут?", bg="#7B68EE", fg="white", font=("Arial", 16))
        label.pack(pady=20)

        self.name_entry = tk.Entry(self.main_frame, font=("Arial", 14))
        self.name_entry.pack(pady=10)

        button = tk.Button(self.main_frame, text="Сохранить имя", bg="#4169E1", fg="white", command=self.save_name, font=("Arial", 14))
        button.pack(pady=10)

    def save_name(self):
        self.name = self.name_entry.get().strip()
        if not self.name:
            messagebox.showwarning("Ошибка", "Имя не может быть пустым!")
            return
        self.init_main_menu()


#главный экран
    def init_main_menu(self):
        self.clear_frame()
        label = tk.Label(self.main_frame, text=f"Привет, {self.name}!", bg="#c40e41", fg="white", font=("Arial", 16))
        label.pack(pady=20)

        programs = [
            ("Программа 1: Ввод имени", self.run_program1),
            ("Программа 2: Математические операции", self.run_program2),
            ("Программа 3: Список случайных чисел", self.run_program3),
            ("Программа 4: Работа с файлами", self.run_program4),
            ("Что сегодня в кинотеатре?", self.run_program5)
        ]

        for text, command in programs:
            button = tk.Button(self.main_frame, text=text, command=command, bg="#c40e41", fg="white", font=("Arial", 14))
            button.pack(pady=10)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def run_program1(self):
        self.clear_frame()
        label = tk.Label(self.main_frame, text=f"Привет, {self.name}!", bg="#c40e41", fg="white", font=("Arial", 16))
        label.pack(pady=20)

        button_back = tk.Button(self.main_frame, text="Назад", bg="#c40e41", fg="white", command=self.init_main_menu, font=("Arial", 14))
        button_back.pack(pady=10)


#программа вторая

    def run_program2(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Введите первое число:", bg="#c40e41", fg="white", font=("Arial", 14)).pack(pady=5)
        num1_entry = tk.Entry(self.main_frame, bg="#c2baf7", fg="white", font=("Arial", 14))
        num1_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Введите второе число:", bg="#c40e41", fg="white", font=("Arial", 14)).pack(pady=5)
        num2_entry = tk.Entry(self.main_frame, bg="#c2baf7", fg="white", font=("Arial", 14))
        num2_entry.pack(pady=5)

        tk.Label(self.main_frame, text="Выберите операцию (+, -, *, /, **):", bg="#c40e41", fg="white", font=("Arial", 14)).pack(pady=5)
        operation_entry = tk.Entry(self.main_frame, bg="#c2baf7", fg="white", font=("Arial", 14))
        operation_entry.pack(pady=5)

        result_label = tk.Label(self.main_frame, bg="#c2baf7", fg="white", font=("Arial", 14))
        result_label.pack(pady=10)

        def calculate():
            try:
                num1 = float(num1_entry.get())
                num2 = float(num2_entry.get())
                oper = operation_entry.get().strip()
                if oper == "+":
                    result = num1 + num2
                elif oper == "-":
                    result = num1 - num2
                elif oper == "*":
                    result = num1 * num2
                elif oper == "**":
                    result = num1 ** num2
                elif oper == "/":
                    if num2 == 0:
                        result_label.config(text="На 0 делить нельзя!".upper())
                        return
                    result = num1 / num2
                else:
                    result_label.config(text="Некорректная операция!", fg="white",)
                    return
                result_label.config(bg="#c40e41", fg="white", text=f"Ответ: {result}")
            except ValueError:
                result_label.config(text="Ошибка ввода!", fg="white",)

        button_calculate = tk.Button(self.main_frame, text="Вычислить", bg="#c40e41", fg="white", command=calculate, font=("Arial", 14))
        button_calculate.pack(pady=10)

        button_back = tk.Button(self.main_frame, text="Назад", bg="#c40e41", fg="white", command=self.init_main_menu, font=("Arial", 14))
        button_back.pack(pady=10)



#третья прога

    def run_program3(self):
        self.clear_frame()

        random_numbers = [random.randint(0, 20) for _ in range(10)]
        sorted_numbers = sorted(random_numbers)
        min_number = min(random_numbers)
        max_number = max(random_numbers)
        sum_numbers = sum(random_numbers)

        tk.Label(self.main_frame, text=f"Список случайных чисел: {random_numbers}", bg="#c40e41", fg="white", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.main_frame, text=f"Сортировка: {sorted_numbers}", bg="#c40e41", fg="white", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.main_frame, text=f"Минимум: {min_number}, Максимум: {max_number}", bg="#c40e41", fg="white", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.main_frame, text=f"Сумма: {sum_numbers}", bg="#c40e41", fg="white", font=("Arial", 12)).pack(pady=5)

        button_back = tk.Button(self.main_frame, text="Назад", bg="#c40e41", fg="white", command=self.init_main_menu, font=("Arial", 14))
        button_back.pack(pady=10)


#прога 4

    def run_program4(self):
        self.clear_frame()

        def create_file(filename):
            with open(os.path.join(self.folder_path, filename), 'w') as file:
                for _ in range(10):
                    file.write(f"{random.randint(1, 10)}\n")
            messagebox.showinfo("Успех", f"Файл '{filename}' создан.")

        def select_file():
            filepath = filedialog.askopenfilename(initialdir=self.folder_path, title="Выберите файл",
                                                  filetypes=(("C:/Users/Angelina/Desktop/borisov", "*.txt"), ("All files", "*.*")))
            if filepath:
                with open(filepath, 'r') as file:
                    numbers = [int(line.strip()) for line in file]
                avg = sum(numbers) / len(numbers)
                messagebox.showinfo("Среднее значение", f"Среднее значение чисел: {avg}")
            else:
                messagebox.showwarning("Ошибка", "Файл не выбран.")

        button1 = tk.Button(self.main_frame, text="Создать файл", bg="#c40e41", fg="white", command=lambda: create_file("file1.txt"),
                            font=("Arial", 14))
        button1.pack(pady=10)

        button2 = tk.Button(self.main_frame, text="Выбрать файл", bg="#c40e41", fg="white", command=select_file, font=("Arial", 14))
        button2.pack(pady=10)

        button_back = tk.Button(self.main_frame, text="Назад", bg="#c40e41", fg="white", command=self.init_main_menu, font=("Arial", 14))
        button_back.pack(pady=10)


#конотеатр 
  
    def run_program5(self):
        self.clear_frame()

        kino1 = Session("Шрек часть первая", 2001, 200, "19-11-2024", "20:00")
        kino2 = Session("Золотой компас", 2007, 180, "19-11-2024", "22:00")

        info1 = kino1.session_info()
        info2 = kino2.session_info()

        label1 = tk.Label(self.main_frame, text=info1, bg="#c40e41", fg="white", font=("Arial", 14), justify="left")
        label1.pack(pady=20)

        label2 = tk.Label(self.main_frame, text=info2, bg="#c40e41", fg="white", font=("Arial", 14), justify="left")
        label2.pack(pady=20)

        button_back = tk.Button(self.main_frame, text="Назад", bg="#c40e41", fg="white", command=self.init_main_menu, font=("Arial", 14))
        button_back.pack(pady=10)


if __name__ == "__main__":
    app = Application()
    app.mainloop()

    print('Программа закрыта')