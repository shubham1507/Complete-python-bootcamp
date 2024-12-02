class Person:
    def __init__(self, name, phone_number, address):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = ""

    def update_contact(self, phone_number, address):
        self.phone_number = phone_number
        self.address = address
        print(f"The contact updated to {self.phone_number}, {self.address}")


class Employee(Person):
    def __init__(self, name, empID):
        super().__init__(name=name, phone_number="", address="")
        self.employee_number = empID

    def promote(self):
        print(f"{self.name} has been promoted")

    def retire(self):
        print(f"{self.name} has been retired")


class Courier(Person):
    def __init__(self, name):
        # Provide default values for phone_number and address
        super().__init__(name=name, phone_number="", address="")

    def deliver_packages(self, package):
        print(f"{self.name} has delivered {package}")


# Create an Employee instance
new_joinee = Employee("Shubham", "8390246938")
new_joinee.email = "shubham.joshi@teksystemsindia.com"
print(new_joinee.email)

# Create a Courier instance
new_courier = Courier("Shubham")
new_courier.deliver_packages("Kurta")
new_courier.update_contact("8390-24-6938", "old mondha, Nanded")
print(new_courier.address)
