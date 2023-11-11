class Phone:
    def __init__(self, surname, name, patronymic, address, number, local_calls_time, long_distance_calls_time):
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__address = address
        self.__number = number
        self.__local_calls_time = local_calls_time
        self.__long_distance_calls_time = long_distance_calls_time
    @property
    def local_calls_time(self):
        return self.__local_calls_time
    @local_calls_time.setter
    def local_calls_time(self, time):
        self.__local_calls_time = time
    @property
    def long_distance_calls_time(self):
        return self.__long_distance_calls_time
    @long_distance_calls_time.setter
    def long_distance_calls_time(self, time):
        self.__long_distance_calls_time = time
