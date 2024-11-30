import tkinter as tk
from tkinter import messagebox, filedialog
import random
import os
<<<<<<< HEAD
from PIL import Image
# import ttkbootstrap as ttk

print('Программа открыта')

#кинотеартр

class Kinoteatr:
    def __init__(self, nameFilms, yerFilm=2015, cena=150):
        self.nameFilms = nameFilms  
        self.yerFilm = yerFilm  
        self.cena = cena  
=======
import requests

print('Программа открыта')

# Кинотеатр
'''Работа с методом в программе кинотеатр'''

class Kinoteatr:
    def __init__(self, nameFilms, yerFilm=2015, cena=150):
        self.nameFilms = nameFilms
        self.yerFilm = yerFilm
        self.cena = cena
>>>>>>> newbranch

    def filmTiket(self):
        return f"Фильм: {self.nameFilms} / Год: {self.yerFilm} / Цена: {self.cena} рублей"

<<<<<<< HEAD
=======
'''Работа с классами (дотсаем сезоны) в программе кинотеатр'''
>>>>>>> newbranch

class Session(Kinoteatr):
    def __init__(self, nameFilms, yerFilm=2015, cena=150, date="7-03-2001", start_time="19:00"):
        super().__init__(nameFilms, yerFilm, cena)
<<<<<<< HEAD
        self.date = date  
        self.start_time = start_time  
=======
        self.date = date
        self.start_time = start_time
>>>>>>> newbranch

    def session_info(self):
        film_info = self.filmTiket()
        return f"Сеанс фильма {self.nameFilms} состоится {self.date} в {self.start_time}.\n{film_info}"

<<<<<<< HEAD

#натройки приложения
=======
    # Функция для получения погоды
    '''Функция для получения погоды'''

    def get_weather(self):
        api_key = "b4f8bb70b3ffbeb08a236b40e0e9a507" 
        city = "Ульяновск"
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=ru"

        try:
            response = requests.get(base_url)
            weather_data = response.json()

            if response.status_code == 200 and weather_data.get("cod") != "404":
                temp = round(weather_data["main"]["temp"] - 273.15, 1) 
                weather_desc = weather_data["weather"][0]["description"]
                humidity = weather_data["main"]["humidity"]
                pressure = weather_data["main"]["pressure"]

                return (f"Погода в {city}:\n"
                        f"Температура: {temp}°C\n"
                        f"Описание: {weather_desc}\n"
                        f"Влажность: {humidity}%\n"
                        f"Давление: {pressure} hPa")
            else:
                return "Не удалось получить данные о погоде."
        except Exception as e:
            return f"Ошибка получения данных: {str(e)}"


# Настройки приложения
'''Настройки самого приложение'''
>>>>>>> newbranch

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Programms")
        self.geometry("600x400")
        self.name = ""
<<<<<<< HEAD
        self.folder_path = "C:/Users/error/Desktop/borisov" 
        self.configure(bg="#7B68EE")  

       
=======
        self.folder_path = "C:/Users/error/Desktop/borisov"
        self.configure(bg="#7B68EE")

>>>>>>> newbranch
        self.main_frame = tk.Frame(self, bg="#7B68EE")
        self.main_frame.pack(fill="both", expand=True)

        self.init_name_screen()


<<<<<<< HEAD
#ввод имени
    def init_name_screen(self):

=======
    '''Операция с выводом на экран'''

# Ввод имени
    def init_name_screen(self):
>>>>>>> newbranch
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


<<<<<<< HEAD
#главный экран
=======
    '''Главный экрна приложеня'''

# Главный экран
>>>>>>> newbranch
    def init_main_menu(self):
        self.clear_frame()
        label = tk.Label(self.main_frame, text=f"Привет, {self.name}!", bg="#c40e41", fg="white", font=("Arial", 16))
        label.pack(pady=20)

<<<<<<< HEAD
=======
        '''Все функции приложения'''

>>>>>>> newbranch
        programs = [
            ("Программа 1: Ввод имени", self.run_program1),
            ("Программа 2: Математические операции", self.run_program2),
            ("Программа 3: Список случайных чисел", self.run_program3),
            ("Программа 4: Работа с файлами", self.run_program4),
<<<<<<< HEAD
            ("Что сегодня в кинотеатре?", self.run_program5)
=======
            ("Что сегодня в кинотеатре?", self.run_program5),
            ("Погода в Ульяновске", self.run_weather_program)  
>>>>>>> newbranch
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


<<<<<<< HEAD
#программа вторая
=======
# Программа 2: Математические операции

    '''Программа с мат.операциями'''
>>>>>>> newbranch

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

<<<<<<< HEAD
=======
        '''Функция подсчета с мат.операциями'''

>>>>>>> newbranch
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


<<<<<<< HEAD

#третья прога
=======
# Программа 3: Список случайных чисел

    '''Программа со случаными числами'''
>>>>>>> newbranch

    def run_program3(self):
        self.clear_frame()

<<<<<<< HEAD
=======
        '''Список что умеет программа'''

>>>>>>> newbranch
        random_numbers = [random.randint(0, 20) for _ in range(10)]
        sorted_numbers = sorted(random_numbers)
        min_number = min(random_numbers)
        max_number = max(random_numbers)
        sum_numbers = sum(random_numbers)

        tk.Label(self.main_frame, text=f"Список случайных чисел: {random_numbers}", bg="#c40e41", fg="white", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.main_frame, text=f"Сортировка: {sorted_numbers}", bg="#c40e41", fg="white", font=("Arial", 12)).pack(pady=5)
<<<<<<< HEAD
        tk.Label(self.main_frame, text=f"Минимум: {min_number}, Максимум: {max_number}", bg="#c40e41", fg="white", font=("Arial", 12)).pack(pady=5)
=======
        tk.Label(self.main_frame, text=f"Минимум: {min_number}", bg="#c40e41", fg="white", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.main_frame, text=f"Максимум: {max_number}", bg="#c40e41", fg="white", font=("Arial", 12)).pack(pady=5)
>>>>>>> newbranch
        tk.Label(self.main_frame, text=f"Сумма: {sum_numbers}", bg="#c40e41", fg="white", font=("Arial", 12)).pack(pady=5)

        button_back = tk.Button(self.main_frame, text="Назад", bg="#c40e41", fg="white", command=self.init_main_menu, font=("Arial", 14))
        button_back.pack(pady=10)


<<<<<<< HEAD
#прога 4
=======
# Программа 4: Работа с файлами

    '''Программа работа с файлами'''
>>>>>>> newbranch

    def run_program4(self):
        self.clear_frame()

<<<<<<< HEAD
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
=======
        '''Сохранение'''

        def save_to_file():
            text = text_area.get("1.0", "end-1c")
            with open(os.path.join(self.folder_path, "output.txt"), "w") as file:
                file.write(text)
            messagebox.showinfo("Готово", "Текст сохранён в output.txt")

            '''Открытие'''

        def open_file():
            file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Текстовые файлы", "*.txt")])
            if file_path:
                with open(file_path, "r") as file:
                    content = file.read()
                text_area.delete("1.0", "end")
                text_area.insert("1.0", content)

        text_area = tk.Text(self.main_frame, width=50, height=10, font=("Arial", 12))
        text_area.pack(pady=10)

        button_save = tk.Button(self.main_frame, text="Сохранить в файл", bg="#c40e41", fg="white", command=save_to_file, font=("Arial", 14))
        button_save.pack(pady=5)

        button_open = tk.Button(self.main_frame, text="Открыть файл", bg="#c40e41", fg="white", command=open_file, font=("Arial", 14))
        button_open.pack(pady=5)
>>>>>>> newbranch

        button_back = tk.Button(self.main_frame, text="Назад", bg="#c40e41", fg="white", command=self.init_main_menu, font=("Arial", 14))
        button_back.pack(pady=10)

<<<<<<< HEAD

#конотеатр 
    def run_program5(self):
        self.clear_frame()

        kino = Session("Шрек часть первая", 2001, 200, "19-11-2024", "20:00")
        info = kino.session_info()

        label = tk.Label(self.main_frame, text=info, bg="#c40e41", fg="white", font=("Arial", 14), justify="left")
        label.pack(pady=20)



        # canvas = self(self, height=400, width=700)
        # image = Image.open("C:/Users/Angelina/Desktop/borisov/img.jpg")
        # photo = ImageTk.PhotoImage(image)
        # image = canvas.create_image(0, 0, anchor='nw',image=photo)

        img=Image.open('C:/Users/Angelina/Desktop/borisov/img.jpg')
        img.show()

=======
# Программа 5: Кинотеатр

    '''Кинотеатр'''

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

# Программа 6: Погода


    '''Самая функция погоды'''

    def run_weather_program(self):
        self.clear_frame()

        session = Session(nameFilms="Терминатор", yerFilm=1985, cena=180, date="01-12-2024", start_time="21:00")
        weather_info = session.get_weather()

        label = tk.Label(self.main_frame, text=weather_info, bg="#c40e41", fg="white", font=("Arial", 14))
        label.pack(pady=20)

>>>>>>> newbranch
        button_back = tk.Button(self.main_frame, text="Назад", bg="#c40e41", fg="white", command=self.init_main_menu, font=("Arial", 14))
        button_back.pack(pady=10)



<<<<<<< HEAD
=======
        '''Вызов всего приложения'''
>>>>>>> newbranch
if __name__ == "__main__":
    app = Application()
    app.mainloop()

<<<<<<< HEAD
    print('Программа закрыта')
=======
>>>>>>> newbranch
