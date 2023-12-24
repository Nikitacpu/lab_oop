from tkinter import *  # Импортируем все из библиотеки tkinter
import random  # Импортируем модуль random для генерации случайных чисел
def throw_dice():  # Определяем функцию, которая будет вызываться при нажатии кнопки "Бросить кубик"
    lab.configure(text=str(random.randint(1, 6)), fg='purple', font=('Arial', 18))  # Меняем текст метки на случайное число от 1 до 6, размер шрифта на 20
window = Tk()  # Создаем окно
window.title("Бросок кубика")  # Устанавливаем заголовок окна
window.geometry('400x400')  # Устанавливаем размер окна
lab = Label(window, text="Брось кубик", fg='blue', font=('Arial', 18))  # Создаем метку с текстом "Брось кубик"
lab.pack()  # Размещаем метку по центру  в окне
btn = Button(window, text='Бросить кубик', font=('Arial',14), command=throw_dice)  # Создаем кнопку "Бросить кубик", которая вызывает функцию throw_dice при нажатии
btn.pack()  # Размещаем кнопку  по центру в   окне
window.mainloop()  # Запускаем главный цикл обработки событий
