class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getSquare(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

    def getRatio(self):
        square = self.getSquare()
        perimeter = self.getPerimeter()
        if perimeter == 0:
            return 0
        return square / perimeter

rectangle = Rectangle(5, 3)
print("Площадь прямоугольника:", rectangle.getSquare())
print("Периметр прямоугольника:", rectangle.getPerimeter())
print("Отношение площади к периметру:", rectangle.getRatio())