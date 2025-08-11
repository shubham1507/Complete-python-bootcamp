# Address class (to be reused)
class Address:
    def __init__(self, city, pincode):
        self.city = city
        self.pincode = pincode

    def __repr__(self):
        return f"{self.city} - {self.pincode}"


# Person class uses Address via composition
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address  # Composition: Person has an Address

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"


# Reusability: The Address class can be reused for many persons
addr1 = Address("Pune", "411021")
addr2 = Address("Mumbai", "400001")

p1 = Person("Shubham", 30, addr1)
p2 = Person("Amit", 25, addr2)

# Display info
print(p1.display_info())
print(p2.display_info())
