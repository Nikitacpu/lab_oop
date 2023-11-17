# Определение класса Vector
class Vector:
    # Конструктор класса
    def __init__(self, *args):
        # Инициализация атрибута values, который хранит целые числа в порядке неубывания
        self.values = sorted([n for n in args if isinstance(n, int)])
    # Переопределение метода __str__ для вывода экземпляра класса в удобном формате
    def __str__(self):
        # Если вектор не пустой, выводим его значения, иначе выводим "Пустой вектор"
        return f"Вектор({', '.join(map(str, self.values))})" if self.values else "Пустой вектор"
    # Переопределение метода __add__ для сложения вектора с числом или другим вектором
    def __add__(self, other):
        # Если other - это число, увеличиваем каждое значение вектора на это число
        if isinstance(other, int):
            return Vector(*(value + other for value in self.values))
        # Если other - это вектор такой же длины, складываем соответствующие элементы
        elif isinstance(other, Vector) and len(self.values) == len(other.values):
            return Vector(*(self.values[i] + other.values[i] for i in range(len(self.values))))
        # Если other - это не число и не вектор, выводим сообщение об ошибке
        else:
            return f"Вектор нельзя сложить с {other}"
    # Переопределение метода __mul__ для умножения вектора на число или другой вектор
    def __mul__(self, other):
        # Если other - это число, умножаем каждое значение вектора на это число
        if isinstance(other, int):
            return Vector(*(value * other for value in self.values))
        # Если other - это вектор такой же длины, умножаем соответствующие элементы
        elif isinstance(other, Vector) and len(self.values) == len(other.values):
            return Vector(*(self.values[i] * other.values[i] for i in range(len(self.values))))
        # Если other - это не число и не вектор, выводим сообщение об ошибке
        else:
            return f"Вектор нельзя умножать с {other}"
# Создание экземпляра класса Vector
v1 = Vector(1, 2, 3)
# Вывод экземпляра класса Vector
print(v1)  # печатает "Вектор(1, 2, 3)"

# Создание экземпляра класса Vector
v2 = Vector(3, 4, 5)
# Вывод экземпляра класса Vector
print(v2)  # печатает "Вектор(3, 4, 5)"
# Сложение двух векторов
v3 = v1 + v2
# Вывод результата сложения
print(v3)  # печатает "Вектор(4, 6, 8)"
# Сложение вектора и числа
v4 = v3 + 5
# Вывод результата сложения
print(v4)  # печатает "Вектор(9, 11, 13)"
# Умножение вектора на число
v5 = v1 * 2
# Вывод результата умножения
print(v5)  # печатает "Вектор(2, 4, 6)"
# Попытка сложить вектор и строку
print(v5 + 'hi')  # печатает "Вектор нельзя сложить с hi"
