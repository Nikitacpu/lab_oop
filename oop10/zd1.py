# Определение класса Transport
class Transport:
    # Инициализация объекта класса
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand  # Бренд транспорта
        self.max_speed = max_speed  # Максимальная скорость
        self.kind = kind  # Тип транспорта
    # Метод для представления объекта в виде строки
    def __str__(self):
        return f"Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч"
# Определение класса Car, наследника класса Transport
class Car(Transport):
    # Инициализация объекта класса
    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind='Car')  # Вызов инициализатора родительского класса
        self.mileage = mileage  # Пробег
        self.gasoline_residue = gasoline_residue  # Остаток бензина
    # Свойство для получения остатка бензина
    @property
    def gasoline(self):
        return f"Осталось бензина на {self.gasoline_residue} л"
    # Свойство для установки остатка бензина
    @gasoline.setter
    def gasoline(self, value):
        if isinstance(value, int):  # Проверка, является ли значение целым числом
            self.gasoline_residue += value  # Увеличение остатка бензина
            print(f'Объем топлива увеличен на {value} л и составляет {self.gasoline_residue} л')
        else:
            print("Ошибка заправки автомобиля")  # Сообщение об ошибке
# Определение класса Boat, наследника класса Transport
class Boat(Transport):
    # Инициализация объекта класса
    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind='Boat')  # Вызов инициализатора родительского класса
        self.owners_name = owners_name  # Имя владельца
    # Метод для представления объекта в виде строки
    def __str__(self):
        return f"Этой лодкой марки {self.brand} владеет {self.owners_name}"
# Определение класса Plane, наследника класса Transport
class Plane(Transport):
    # Инициализация объекта класса
    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind='Plane')  # Вызов инициализатора родительского класса
        self.capacity = capacity  # Вместимость
    # Метод для представления объекта в виде строки
    def __str__(self):
        return f"Самолет марки {self.brand} вмещает в себя {self.capacity} людей"
