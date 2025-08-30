class Person:
    # class var (shared by all)
    species = "Human"
    
    def __init__(self, name, age):
        # instance var unique to each other
        self.name = name
        self.age = age 
        
    # instance method (work on object only)
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Species: {Person.species}"
        
    # class method (works at class-level data)
    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species
        return f"Species changed to {cls.species}"
        
    # static mettod (utility function)
    
    @staticmethod
    def is_adult(age):
        return age>=18
        
p1 = Person("Shubham", 31)
p2 = Person("Amit", 32)

#calling instance method
print("Instance Method:")
print(p1.display_info())
print(p2.display_info())

# calling class method

print("\nClass Method:")
print(Person.change_species("Sapiens"))
print(p1.display_info())
print(p2.display_info())

# calling static method

print("\n static Method:")

print(f" IS p1 adult?{Person.is_adult(p1.age)}")
print(f" IS p2 adult?{Person.is_adult(p2.age)}")
