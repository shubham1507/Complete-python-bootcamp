class Person:
    def __init__(self, name, age, street, city, pincode):
        self.name = name
        self.age = age
        # Creating object of inner class Address
        self.address = self.Address(street, city, pincode)
        
    def show_details(self):
        return f"Name: {self.name},Age:{self.age} and Address:{self.address.show_address()}"
        
    class Address:
        def __init__(self, street, city, pincode):
            self.street = street
            self.city = city
            self.pincode = pincode
            
        def show_address(self):
            return f"{self.street} {self.city}-{self.pincode}"
        
# Creating Person object (Address object gets created internally)
p1 = Person("Shubham", 30, "MG Road", "Pune", 411001)

print(p1.show_details())

# Accessing inner class object directly
addr = p1.address
print("City:", addr.city)
