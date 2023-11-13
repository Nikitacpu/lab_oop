# Определение родительского класса "WebStore"
class WebStore:
    # Конструктор класса
    def __init__(self, shop_name, item_name, origin_country, payment_method, total_amount, transaction_date, buyer_fullname):
        self.shop_name = shop_name  # Название магазина
        self.item_name = item_name  # Название товара
        self.origin_country = origin_country  # Страна производитель
        self.payment_method = payment_method  # Вид оплаты
        self.total_amount = total_amount  # Сумма покупки
        self.transaction_date = transaction_date  # Дата продажи
        self.buyer_fullname = buyer_fullname  # ФИО покупателя
    # Метод для вывода информации об экземпляре класса
    def __str__(self):
        # Возвращает строку с полной информацией об экземпляре класса
        return (f'Shop: {self.shop_name}, Item: {self.item_name}, Origin Country: {self.origin_country}, Payment Method: {self.payment_method},'
                f' Total Amount: {self.total_amount}, Transaction Date: {self.transaction_date}, Buyer: {self.buyer_fullname}')
# Определение дочернего класса "LivingSpaceFurniture"
class LivingSpaceFurniture(WebStore):
    # Конструктор класса
    def __init__(self, shop_name, item_name, origin_country, payment_method, total_amount, transaction_date, buyer_fullname, furniture_kind, maker):
        super().__init__(shop_name, item_name, origin_country, payment_method, total_amount, transaction_date, buyer_fullname)  # Вызов конструктора родительского класса
        self.furniture_kind = furniture_kind  # Тип мебели
        self.maker = maker  # Производитель
    # Метод для вывода информации об экземпляре класса
    def __str__(self):
        # Возвращает строку с полной информацией об экземпляре класса, включая тип мебели и производителя
        return super().__str__() + f', Furniture Kind: {self.furniture_kind}, Maker: {self.maker}'
# Определение дочернего класса "KitchenSet"
class KitchenSet(WebStore):
    # Конструктор класса
    def __init__(self, shop_name, item_name, origin_country, payment_method, total_amount, transaction_date, buyer_fullname, length, height, width, material):
        super().__init__(shop_name, item_name, origin_country, payment_method, total_amount, transaction_date, buyer_fullname)  # Вызов конструктора родительского класса
        self.length = length  # Длина
        self.height = height  # Высота
        self.width = width  # Ширина
        self.material = material  # Материал
    # Метод для вывода информации об экземпляре класса
    def __str__(self):
        # Возвращает строку с полной информацией об экземпляре класса, включая размеры и материал мебели
        return super().__str__() + f', Length: {self.length}, Height: {self.height}, Width: {self.width}, Material: {self.material}'
# Определение дочернего класса "BathFurniture"
class BathFurniture(WebStore):
    # Конструктор класса
    def __init__(self, shop_name, item_name, origin_country, payment_method, total_amount, transaction_date, buyer_fullname):
        super().__init__(shop_name, item_name, origin_country, payment_method, total_amount, transaction_date, buyer_fullname)  # Вызов конструктора родительского класса
    # Метод для вывода информации об экземпляре класса
    def __str__(self):
        # Возвращает строку с полной информацией об экземпляре класса
        return super().__str__()
