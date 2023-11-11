from student_list import StudentList
# Создаем список студентов
students = StudentList()
# Добавляем в список десять студентов
for _ in range(10):
    name = input('Введите фамилию и имя студента: ')
    group_number = input('Введите номер группы: ')
    students.add_student(name, group_number)
# Сортируем студентов по среднему баллу и выводим информацию о них
students.sort_by_gpa()
students.print_all()
