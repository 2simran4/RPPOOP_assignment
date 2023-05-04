class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(sides=4)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)

    def get_area(self):
        return super().get_area()

    def get_perimeter(self):
        return super().get_perimeter()

rectangle = Rectangle(width=5, height=10)
print(rectangle.get_area())  # Output: 50
print(rectangle.get_perimeter())  # Output: 30


square = Square(side=7)
print(square.get_area())  # Output: 49
print(square.get_perimeter())  # Output: 28

