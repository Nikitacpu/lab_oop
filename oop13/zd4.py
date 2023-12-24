from tkinter import *
from math import *

def calculate():
    x = float(x_entry.get())
    result = 1.8 + log(4*2/7) - tan(sin(5*x/3))
    result_label.config(text=result)

window = Tk()
window.title("Формула")
window.geometry('400x400')  # Устанавливаем размер окна

x_label = Label(window, text="Подсчет по формуле ", fg='blue',font=("Arial", 14))
x_label.place(x=60, y=20)  # Размещаем метку с помощью метода place

v_label = Label(window, text="выражение= ", font=("Arial", 14))
v_label.place(x=40, y=100)  # Размещаем метку с помощью метода place

x_entry = Entry(window, font=("Arial", 14))
x_entry.place(x=45, y=50)  # Размещаем поле ввода с помощью метода place

result_label = Label(window, text="", font=("Arial", 14))  # Добавляем метку для результата
result_label.place(x=170, y=100)  # Размещаем метку результата с помощью метода place

calc_button = Button(window, text="Вычислить", command=calculate)  # Добавляем кнопку для вызова функции calculate
calc_button.place(x=100, y=80)  # Размещаем кнопку с помощью метода place

window.mainloop()  # Запускаем главный цикл обработки событий
