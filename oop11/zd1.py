# Определение класса File
class File:
    # Конструктор класса File
    def __init__(self, name):
        # Инициализация атрибута name
        self.name = name
    # Метод для возвращения строкового представления объекта
    def __str__(self):
        return f'Файл: {self.name}'
# Определение класса zhtenie, который наследуется от класса File
class zhtenie(File):
    # Конструктор класса zhtenie
    def __init__(self, name):
        # Вызов конструктора родительского класса
        super().__init__(name)
    # Метод для возвращения строкового представления объекта
    def __str__(self):
        return f'Файл для чтения: {self.name}'
# Определение класса zapisi, который наследуется от класса File
class zapisi(File):
    # Конструктор класса zapisi
    def __init__(self, name):
        # Вызов конструктора родительского класса
        super().__init__(name)
    # Метод для возвращения строкового представления объекта
    def __str__(self):
        return f'Файл для записи: {self.name}'
# Определение класса zapisi_zhtenie, который наследуется от классов zhtenie и zapisi
class zapisi_zhtenie(zhtenie, zapisi):
    # Конструктор класса zapisi_zhtenie
    def __init__(self, name):
        # Вызов конструктора родительского класса
        super().__init__(name)
    # Метод для возвращения строкового представления объекта
    def __str__(self):
        return f'Файл для чтения и записи: {self.name}'
