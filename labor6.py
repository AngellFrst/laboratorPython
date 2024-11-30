from tkinter import *
import random
import os
import tkinter as tk
from tkinter import filedialog


print("Программа запущена")

root = Tk()
root['bg'] = '#7B68EE'  #цвет фона 
root.title('Programs')
root.geometry('700x500')


frame = Frame(
   root, #Обязательный параметр, который указывает окно для размещения Frame.
   padx = 10, #Задаём отступ по горизонтали.
   pady = 10 #Задаём отступ по вертикали.
)
frame.pack(expand=True)

#прогрмма первая


name_l = Label(
   frame,
   text="Привет, как тебя зовут?",
)
name_l.grid(row=1, column=1)

name_vvod = Entry(
   frame,
)
name_vvod.grid(row=4, column=1)

name_btn = Button(
   frame, 
   text='Ответить', #Надпись на кнопке.
)
name_btn.grid(row=5, column=1 ) 

root.resizable(width=False, height=False)
root.mainloop()
print("Программа закрыта")





