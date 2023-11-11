# main.py
from patient import Patient
def input_patient_data():
    """
    Функция для ввода данных пациента пользователем.
    """
    fam = input("Введите фамилию: ")
    name = input("Введите имя: ")
    otcestvo = input("Введите отчество: ")
    address = input("Введите адрес: ")
    nomer = int(input("Введите номер медицинской карты: "))
    bol = input("Введите диагноз: ")
    return Patient(fam, name,otcestvo  , address, nomer, bol)
def print_info(patients):
    """
    Функция для вывода списка пациентов, номер медицинской карты которых находится в заданном интервале.
    """
    for patient in patients:
        if 0 < patient.nomer <= 100:
            patient.print_info()
# Создаем массив объектов класса Patient
patients = [   input_patient_data()
               for k in range(2)]
# Выводим список пациентов с номером медицинской карты в заданном интервале
print_info(patients)