Инициализация
класса
Student.
"""
self.name = name
self.group_number = group_number
self.academic_performance = [random.randint(1, 10) for _ in range(5)]
self.gpa_scores = sum(self.academic_performance) / 5

def print_info(self):
"""
Метод
для
вывода
информации
о
студенте.
"""
print(f'ФИ: {self.name}\n'
      f'Номер группы: {self.group_number}\n'
      f'Успеваемость: {self.academic_performance}\n'
      f'Средний балл: {self.gpa_scores}\n')
#ZD3.py 
# student.py
import random

class Student:
"""
    Класс Student для представления студента.
    """
    def __init__(self, name, group_number):
        """
affFW
G

g

G
G
