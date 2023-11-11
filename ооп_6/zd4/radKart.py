from kart import Kart
class RadKart:
    """
    Класс RadKart для представления грядки картошки.
    """
    def __init__(self, bon):
        """
        Инициализация класса RadKart.
        """
        self.karts = [Kart(i)
                      for i in range(1, bon + 1)]
    def mature_all(self):
        """
        Метод для роста всей картошки на грядке.
        """
        print("Картошка прорастает!")
        for kart in self.karts:
            kart.mature()
            kart.display_info()
    def all_mature(self):
        """
        Метод для проверки зрелости всей картошки на грядке.
        """
        return all([kart.is_mature() for kart in self.karts])