#Operator Overloading
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.width + other.width, self.height + other.height)
        else:
            return Rectangle(self.width + other, self.height + other)

    def __str__(self):
        return f"Rectangle ({self.width}, {self.height})"

r1 = Rectangle(2, 3)
r2 = Rectangle(4, 5)

r3 = r1 + r2
print(r3)           # Output: Rectangle (6, 8)

r4 = r1 + 2
print(r4)           # Output: Rectangle (4, 5)

#Operator Overriding
class Animal:
    def make_sound(self):
        print("Generic Animal Sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

def make_animal_sound(animal):
    animal.make_sound()

animal = Animal()
dog = Dog()
cat = Cat()

make_animal_sound(animal)

