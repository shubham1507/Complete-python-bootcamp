# 1. Class
class Animal:
    # 2. Constructor/Initializer
    def __init__(self, name, sound):
        self._name = name  # private attribute
        self._sound = sound  # private attribute

    # 4. Getter method
    def get_name(self):
        return self._name

    # 4. Setter method
    def set_name(self, name):
        self._name = name

    # 5. Encapsulation
    # Using private attributes (_name and _sound) to restrict direct access

    def make_sound(self):
        return f"{self._name} says {self._sound}"


# 6. Inheritance
class Dog(Animal):
    def __init__(self, name, sound, breed):
        # Call parent constructor
        super().__init__(name, sound)
        self.breed = breed  # new attribute specific to Dog

    # 8. Overriding Method
    def make_sound(self):
        return f"{self.get_name()} (a {self.breed}) barks '{self._sound}'"

# 7. Abstraction
from abc import ABC, abstractmethod

class Bird(ABC):  # Abstract class
    @abstractmethod
    def fly(self):
        pass  # Abstract method with no implementation

class Sparrow(Bird):  # Concrete class
    def fly(self):
        return "Sparrow is flying."


# 9. Polymorphism
# (a) Duck Typing
class Car:
    def move(self):
        return "The car is moving on the road."

class Plane:
    def move(self):
        return "The plane is flying in the air."

def vehicle_movement(vehicle):
    print(vehicle.move())  # No need to check the type

# (b) Method Overriding (already shown in `Dog`)

# (c) Operator Overloading
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)

# (d) Method Overloading (Not directly supported, but simulated with default arguments)
class Calculator:
    def add(self, a, b=0):
        return a + b


# Usage
# Creating objects
cat = Animal("Cat", "Meow")
print(cat.make_sound())

dog = Dog("Buddy", "Woof", "Golden Retriever")
print(dog.make_sound())

# Abstraction
sparrow = Sparrow()
print(sparrow.fly())

# Duck Typing
car = Car()
plane = Plane()
vehicle_movement(car)
vehicle_movement(plane)

# Operator Overloading
num1 = Number(5)
num2 = Number(10)
print(f"Sum: {num1 + num2}")

# Method Overloading
calc = Calculator()
print(calc.add(3))  # Single argument
print(calc.add(3, 5))  # Two arguments

"""
Explanation:
Class: Animal and Dog are examples of classes.
Object: Instances like cat and dog are objects of their respective classes.
Constructor/Initializer: The __init__ method initializes objects.
Getter and Setter: get_name and set_name provide controlled access to private attributes.
Encapsulation: Attributes like _name and _sound are private and accessed only through methods.
Inheritance: Dog inherits from Animal.
Abstraction: Bird is an abstract class that defines fly but doesn't implement it.
Overriding Method: make_sound is overridden in Dog.
Polymorphism:
Duck Typing: vehicle_movement works for any object with a move method.
Method Overriding: Seen in Dog.
Operator Overloading: The + operator is overloaded in Number.
Method Overloading: Simulated in Calculator with default arguments.


"""
