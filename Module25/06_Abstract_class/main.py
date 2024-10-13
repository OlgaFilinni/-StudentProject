import abc


class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.14

    def __str__(self):
        return f"площадь круга: {self.area()}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


    def __str__(self):
        return f"площадь круга: {self.area()}"


class Triangle(Shape):
    def __init__(self, base, heigh):
        self.base = base
        self.heigh = heigh

    def area(self):
        return 0.5 * self.base * self.heigh


    def __str__(self):
     return f"площадь треугольника: {self.area()}"


# Примеры работы с классом:
# Создание экземпляров классов

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

# Вывод результатов
print("Площадь круга:", circle_area)
print("Площадь прямоугольника:", rectangle_area)
print("Площадь треугольника:", triangle_area)
