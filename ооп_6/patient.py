# patient.py
class Patient:
    """
    Класс Patient для хранения информации о пациенте.
    """
    def __init__(self, fam, name, otcestvo , address, nomer, bol):
        """
        Инициализация класса Patient.
        """
        self.fam = fam
        self.name = name
        self.otcestvo  = otcestvo
        self.address = address
        self.nomer= nomer
        self.bol = bol

    def print_info(self):
        """
        Метод для вывода информации о пациенте.
        """
        print(f"Фамилия: {self.fam},"
              f" Имя: {self.name}, "
              f"Отчество: {self.otcestvo },"
              f" Адрес: {self.address}, "
              f"Номер медицинской карты: {self.nomer},"
              f" Диагноз: {self.bol}")