class City:
    def __init__(self, name):
        self.__name = name  # Инициализируем название города
        self.__buildings = []  # Инициализируем пустой список для хранения зданий в городе

    @property
    def name(self):
        return self.__name  # Геттер для названия города

    @name.setter
    def name(self, value):
        self.__name = value  # Сеттер для названия города

    @property
    def buildings(self):
        return self.__buildings  # Геттер для списка зданий

    def add_building(self, building):
        building.city = self  # Устанавливаем связь между зданием и городом
        self.__buildings.append(building)  # Добавляем здание в список зданий города


class Building:
    def __init__(self, street_name, house_number, base_monthly_payment):
        self.__street_name = street_name  # Инициализируем название улицы
        self.__house_number = house_number  # Инициализируем номер дома
        self.__base_monthly_payment = base_monthly_payment  # Инициализируем базовую ежемесячную оплату
        self.__rooms = []  # Инициализируем пустой список для хранения помещений в здании
        self.__city = None  # Инициализируем город, в котором находится здание

    @property
    def city(self):
        return self.__city  # Геттер для города

    @city.setter
    def city(self, value):
        self.__city = value  # Сеттер для города

    @property
    def street_name(self):
        return self.__street_name  # Геттер для названия улицы

    @street_name.setter
    def street_name(self, value):
        self.__street_name = value  # Сеттер для названия улицы

    @property
    def house_number(self):
        return self.__house_number  # Геттер для номера дома
    @house_number.setter
    def house_number(self, value):
        self.__house_number = value  # Сеттер для номера дома
    @property
    def total_area(self):
        return sum(room.area for room in self.__rooms)  # Геттер для общей площади всех помещений в здании
    @property
    def base_monthly_payment(self):
        return self.__base_monthly_payment  # Геттер для базовой ежемесячной оплаты
    @base_monthly_payment.setter
    def base_monthly_payment(self, value):
        self.__base_monthly_payment = value  # Сеттер для базовой ежемесячной оплаты
    def add_room(self, room):
        room.building = self  # Устанавливаем связь между помещением и зданием
        self.__rooms.append(room)  # Добавляем помещение в список помещений здания
class Room:
    def __init__(self, number, area):
        self.__number = number  # Инициализируем номер помещения
        self.__area = area  # Инициализируем площадь помещения
        self.__building = None  # Инициализируем здание, в котором находится помещение
    @property
    def building(self):
        return self.__building  # Геттер для здания
    @building.setter
    def building(self, value):
        self.__building = value  # Сеттер для здания
    @property
    def number(self):
        return self.__number  # Геттер для номера помещения
    @number.setter
    def number(self, value):
        self.__number = value  # Сеттер для номера помещения
    @property
    def area(self):
        return self.__area  # Геттер для площади помещения
    @area.setter
    def area(self, value):
        self.__area = value  # Сеттер для площади помещения

    def calculate_monthly_payment(self):
        pass  # Метод для расчета ежемесячной оплаты, который будет переопределен в подклассах
class Apartment(Room):
    def __init__(self, number, area, tenants):
        super().__init__(number, area)  # Инициализируем номер и площадь помещения с помощью конструктора родительского класса
        self.__tenants = tenants  # Инициализируем список жильцов квартиры
    @property
    def tenants(self):
        return self.__tenants  # Геттер для списка жильцов
    @tenants.setter
    def tenants(self, value):
        self.__tenants = value  # Сеттер для списка жильцов

    def calculate_monthly_payment(self):
        try:
            if not self.__tenants:
                raise ValueError("В квартире нет жильцов.")  # Выбрасываем исключение, если в квартире нет жильцов
            # Предположим, что ежемесячная оплата равна 10 единицам валюты за каждый квадратный метр
            return 10 * self.__area
        except ValueError as e:
            print(f"Произошла ошибка при расчете ежемесячной оплаты: {e}")  # Обрабатываем исключение и выводим сообщение об ошибке
            return 0
class Office(Room):
    def __init__(self, number, area, company_name, activity_type):
        super().__init__(number, area)  # Инициализируем номер и площадь помещения с помощью конструктора родительского класса
        self.__company_name = company_name  # Инициализируем название компании
        self.__activity_type = activity_type  # Инициализируем вид деятельности компании
    @property
    def company_name(self):
        return self.__company_name  # Геттер для названия компании
    @company_name.setter
    def company_name(self, value):
        self.__company_name = value  # Сеттер для названия компании
    @property
    def activity_type(self):
        return self.__activity_type  # Геттер для вида деятельности компании
    @activity_type.setter
    def activity_type(self, value):
        self.__activity_type = value  # Сеттер для вида деятельности компании
    def calculate_monthly_payment(self):
        try:
            # Предположим, что ежемесячная оплата равна 10 единицам валюты за каждый квадратный метр, как и в Apartment
            return 10 * self.__area
        except Exception as e:
            print(f"Произошла ошибка при расчете ежемесячной оплаты: {e}")  # Обрабатываем исключение и выводим сообщение об ошибке
# Пример использования
city = City("Минск")  # Создаем город Минск
building = Building("Ленина", 1, 100.0)
city.add_building(building)  # Добавляем здание в город
building.add_room(Room(1, 50.0))
building.add_room(Apartment(2, 75.0, ["Васильев"]))  
building.add_room(Office(3, 100.0, "Офиис 1 ", "Офис2 "))
print(building.total_area)  # Выводим общую площадь всех помещений в здании

# Создаем квартиру без жильцов
empty_apartment = Apartment(4, 80.0, [])
building.add_room(empty_apartment)

# Пытаемся рассчитать ежемесячную оплату для квартиры без жильцов
print(empty_apartment.calculate_monthly_payment())

