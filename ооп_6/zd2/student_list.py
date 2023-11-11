from student import Student
class StudentList:
    """
    Класс StudentList для представления списка студентов.
    """
    def __init__(self):
        """
        Инициализация класса StudentList.
        """
        self.students = []
    def add_student(self, name, group_number):
        """
        Метод для добавления студента в список.
        """
        self.students.append(Student(name, group_number))
    def sort_by_gpa(self):
        """
        Метод для сортировки студентов по среднему баллу.
        """
        self.students.sort(key=lambda student: student.gpa_scores)
    def print_all(self):
        """
        Метод для вывода информации обо всех студентах в списке.
        """
        for student in self.students:
            student.print_info()
