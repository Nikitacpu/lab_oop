class Kart:
    """
    Класс Kart для представления картошки.
    """
    vid = ["Посажена", "Росток", "Зелёная", "Зрелая"]

    def __init__(self, id):
        """
        Инициализация класса Kart.
        """
        self.id = id
        self.rost = 0

    def mature(self):
        """
        Метод для роста картошки.
        """
        if self.rost < len(self.vid) - 1:
            self.rost += 1

    def is_mature(self):
        """
        Метод для проверки зрелости картошки.
        """
        return self.rost == len(self.vid) - 1

    def display_info(self):
        """
        Метод для вывода информации о картошке.
        """
        print(f"Картошка {self.id} сейчас {self.vid[self.rost]}")