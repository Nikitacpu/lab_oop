# Класс "Rectangle" (Прямоугольник)
class Rectangle:
    # Конструктор класса
    def __init__(self, a, b):
        # Присваивание значений сторон
        self.a = a
        self.b = b

    # Метод для вычисления площади
    def get_area(self):
        return self.a*self.b

# Класс "Square" (Квадрат)
class Square:
    # Конструктор класса
    def __init__(self, a):
        # Присваивание значения стороны
        self.a = a

    # Метод для вычисления площади
    def get_area(self):
        return self.a**2

# Класс "Circle" (Круг)
class Circle:
    # Конструктор класса
    def __init__(self, r):
        # Присваивание значения радиуса
        self.r = r

    # Метод для вычисления площади
    def get_area(self):
        return 3.14*self.r**2

# Создание объекта класса "Rectangle"
rect1 = Rectangle(3, 4)
# Создание объекта класса "Rectangle"
rect2 = Rectangle(12, 3)

# Создание объекта класса "Square"
sq1 = Square(2)

# Создание объекта класса "Circle"
cir1 = Circle(3)

# Создание списка фигур
figures = [rect1, rect2, sq1, cir1]
# Вывод площади каждой фигуры
for figure in figures:
    print(figure.get_area())
