import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius**2

    def get_circumference(self):
        return 2 * math.pi * self.__radius

# Пример использования:
circle = Circle(5)

area = circle.get_area()
circumference = circle.get_circumference()

print(f"Площадь круга: {area}")
print(f"Длина окружности: {circumference}")