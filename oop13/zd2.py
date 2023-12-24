from tkinter import *  # Импортируем все из библиотеки tkinter

def clicked():  # Определяем функцию, которая будет вызываться при нажатии кнопки "Приветствие"
    lab.configure(text='Первые успехи')  # Меняем текст метки на "Первые успехи"

def close_window():  # Определяем функцию, которая будет вызываться при нажатии кнопки "Закрыть"
    window.destroy()  # Закрываем окно

window = Tk()  # Создаем окно
window.title("Проект 2")  # Устанавливаем заголовок окна
window.geometry('400x100')  # Устанавливаем размер окна

lab = Label(window, text="", font=('Arial', 14))  # Создаем метку с пустым текстом и шрифтом Arial размером 14
lab.grid(column=1, row=0)  # Размещаем метку в окне

btn = Button(window, text='Приветствие', font=('Arial',14), command=clicked)  # Создаем кнопку "Приветствие", которая вызывает функцию clicked при нажатии
btn.grid(column=0, row=1)  # Размещаем кнопку в окне

btn1 = Button(window, text='Закрыть', font=('Arial',14), command=close_window)  # Создаем кнопку "Закрыть", которая вызывает функцию close_window при нажатии
btn1.grid(column=10, row=1)  # Размещаем кнопку в окне

window.mainloop()  # Запускаем главный цикл обработки событий