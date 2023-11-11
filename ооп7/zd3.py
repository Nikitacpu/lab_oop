# Импорт модуля random для генерации случайных чисел
import random

# Определение класса Flower
class Flower:
    # Инициализация атрибутов длины стебля и свежести
    def __init__(self, stem_length, freshess):
        self.stem_length = stem_length
        self.freshess = freshess

    # Определение свойства для длины стебля
    @property
    def stem_length(self):
        return self._stem_length

    # Метод-сеттер для длины стебля с проверкой условий
    @stem_length.setter
    def stem_length(self, value):
        if not isinstance(value, int):
            print('Длинна стебля должна быть числом')
        elif value < 5:
            print('Длинна стебля должна быть минимум 5')
        elif value > 20:
            print('Длинна стебля должна быть максимум 20')
        else:
            self._stem_length = value

    # Определение свойства для свежести
    @property
    def freshess(self):
        return self._freshness

    # Метод-сеттер для свежести с проверкой условий
    @freshess.setter
    def freshess(self, value):
        if not isinstance(value, int):
            print('Уровеень свежости должнен быть числом')
        elif value < 1:
            print('Уровеень свежости должнен быть минимум 1')
        elif value > 10:
            print('Уровеень свежости должнен быть максимум 10')
        else:
            self._freshness = value

# Инициализация списка цветов
f = []
# Создание 5 объектов класса Flower со случайными значениями для длины стебля и свежести
for i in range(5):
    f.append(Flower(int(random.uniform(5, 20)), int(random.uniform(1, 10))))
    print(f'Цветок {i + 1}: длинна стебля {f[i].stem_length}, уровень свежости {f[i].freshess}')

# Сортировка списка цветов по уровню свежести
f.sort(key=lambda i: i.freshess)

# Вывод отсортированного списка цветов
print('Отсортированый букет: ')
for i in range(5):
    print(f'Цветок {i + 1}: - уровень свежости {f[i].freshess}')

# Запрос у пользователя диапазона значений для фильтрации списка цветов
l1 = int(input('введите начальное значение диапазона: '))
l2 = int(input('введите конечное значение диапозона: '))

# Вывод цветков из списка, чья длина стебля находится в заданном диапазоне
for i in range(5):
    if f[i].stem_length >= l1 and f[i].stem_length <= l2:
        print(f'Цветок {i + 1}: - уровень свежости {f[i].freshess}')
