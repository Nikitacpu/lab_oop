# Класс "FlatPoint" (Плоскостная точка)
class FlatPoint:
    # Конструктор класса
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY

    # Метод для вычисления расстояния до другой точки
    def distance(self, otherPoint):
        return math.sqrt((self.coordX - otherPoint.coordX)**2 + (self.coordY - otherPoint.coordY)**2)

    # Метод для вычисления расстояния до начала координат
    def distanceToOrigin(self):
        return math.sqrt(self.coordX**2 + self.coordY**2)

    # Метод для красивого вывода точки
    def __str__(self):
        return f"Flat point with coordinates ({self.coordX}, {self.coordY})"

# Класс "SpacePoint" (Пространственная точка)
class SpacePoint(FlatPoint):
    def __init__(self, coordX, coordY, coordZ):
        super().__init__(coordX, coordY)
        self.coordZ = coordZ

    # Переопределение метода для вычисления расстояния до другой точки
    def distance(self, otherPoint):
        return math.sqrt((self.coordX - otherPoint.coordX)**2 + (self.coordY - otherPoint.coordY)**2 + (self.coordZ - otherPoint.coordZ)**2)

    # Переопределение метода для вычисления расстояния до начала координат
    def distanceToOrigin(self):
        return math.sqrt(self.coordX**2 + self.coordY**2 + self.coordZ**2)

    # Переопределение метода для красивого вывода точки
    def __str__(self):
        return f"Space point with coordinates ({self.coordX}, {self.coordY}, {self.coordZ})"
