#Single level heritance
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "woof")
        self.breed = breed

    def wag_tail(self):
        print(f"{self.name} wags tail")

dog = Dog("Buddy", "Golden Retriever")
dog.make_sound()    # Output: Buddy says woof
dog.wag_tail()      # Output: Buddy wags tail

#Multiple Heritance
class Flying:
    def fly(self):
        print("Flying")

class Swimming:
    def swim(self):
        print("Swimming")

class Duck(Flying, Swimming):
    def quack(self):
        print("Quack")

duck = Duck()
duck.fly()      # Output: Flying
duck.swim()     # Output: Swimming
duck.quack()    # Output: Quack

#Multilevel Inheritance
#Multi-level inheritance is where a child class inherits from a parent class, which itself inherits from another parent class.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

class ElectricCar(Car):
    def __init__(self, make, model, year, doors, battery_capacity):
        super().__init__(make, model, year, doors)
        self.battery_capacity = battery_capacity

car = ElectricCar("Tesla", "Model S", 2022, 4, "100 kWh")
print(car.make)             # Output: Tesla
print(car.doors)            # Output: 4
print(car.battery_capacity) # Output: 100 kWh


