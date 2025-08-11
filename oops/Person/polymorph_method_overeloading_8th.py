class Person:
    def __init__(self, name):
        self.name = name

    # Simulated method overloading using default arguments
    def greet(self, greeting="Hello", times=1):
        """
        If only 'greeting' is given → use default 'times=1'
        If both are given → repeat greeting 'times' times
        """
        return (f"{greeting}, {self.name}! " * times).strip()

    # Simulated method overloading using *args
    def introduce(self, *args):
        """
        Possible calls:
        introduce()
        introduce(age)
        introduce(age, city)
        """
        if len(args) == 0:
            return f"My name is {self.name}."
        elif len(args) == 1:
            return f"My name is {self.name}, I am {args[0]} years old."
        elif len(args) == 2:
            return f"My name is {self.name}, I am {args[0]} years old, from {args[1]}."
        else:
            return "Too many details provided!"


# Create Person object
p1 = Person("Shubham")

# Calling greet() in different ways (method overloading style)
print(p1.greet())                     # Uses defaults
print(p1.greet("Hi"))                  # Changes greeting
print(p1.greet("Good morning", 3))     # Repeats greeting 3 times

# Calling introduce() in different ways
print(p1.introduce())                  # No args
print(p1.introduce(30))                 # One arg
print(p1.introduce(30, "Pune"))         # Two args
