from tkinter import *  # Импортируем все из библиотеки tkinter

def close_window():  # Определяем функцию, которая будет закрывать окно
    window.destroy()  # Уничтожаем окно

window = Tk()  # Создаем главное окно
window.title("Проект 1")  # Устанавливаем заголовок окна
window.geometry('400x100')  # Устанавливаем размер окна

lab = Label(window, text="Моя первая программа", font=('Arial', 14))  # Создаем метку с текстом
lab.pack()  # Размещаем метку в окне

btn = Button(window, text='Закрыть', font=('Arial',14), command=close_window)  # Создаем кнопку, которая будет закрывать окно
btn.pack()  # Размещаем кнопку в окне

window.mainloop()  # Запускаем главный цикл обработки событий