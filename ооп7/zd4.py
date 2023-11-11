# Определение класса Kvartira
class Kvartira:
    # Конструктор класса Kvartira
    def __init__(self, nomer, komnaty, zhilye):
        self.nomer = nomer  # номер квартиры
        self.komnaty = komnaty  # количество комнат в квартире
        self.zhilye = zhilye  # количество проживающих в квартире
# Определение класса Dom
class Dom:
    # Конструктор класса Dom
    def __init__(self):
        self.kvartiry = []  # список квартир в доме
    # Метод для добавления квартиры в дом
    def add_kvartira(self, kvartira):
        self.kvartiry.append(kvartira)
    # Метод для сортировки квартир по количеству комнат
    def sort_kvartiry(self):
        self.kvartiry.sort(key=lambda x: x.komnaty)
    # Метод для поиска квартиры с заданным диапазоном числа проживающих
    def find_kvartira(self, min_zhilye, max_zhilye):
        return [kvartira for kvartira in self.kvartiry if min_zhilye <= kvartira.zhilye <= max_zhilye]
# Создание объектов класса Kvartira
kvartira1 = Kvartira(1, 2, 3)
kvartira2 = Kvartira(2, 3, 4)
kvartira3 = Kvartira(3, 1, 2)
kvartira4 = Kvartira(4, 2, 4)
kvartira5 = Kvartira(5, 3, 5)
# Создание объекта класса Dom и добавление в него квартир
dom = Dom()
dom.add_kvartira(kvartira1)
dom.add_kvartira(kvartira2)
dom.add_kvartira(kvartira3)
dom.add_kvartira(kvartira4)
dom.add_kvartira(kvartira5)
# Сортировка квартир по количеству комнат
dom.sort_kvartiry()
# Поиск квартир с заданным диапазоном числа проживающих
naydennye_kvartiry = dom.find_kvartira(2, 4)
