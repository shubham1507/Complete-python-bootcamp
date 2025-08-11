class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor called for {self.name}")


class Employee(Person):
    def __init__(self, name, emp_id):
        # Overriding the parent's constructor
        super().__init__(name)  # Call parent constructor to set 'name'
        self.emp_id = emp_id    # New property for Employee
        print(f"Employee constructor called for {self.name} with ID {self.emp_id}")


# Creating objects
p1 = Person("Shubham")
e1 = Employee("Amit", 101)

# Accessing attributes
print(f"p1 -> Name: {p1.name}")
print(f"e1 -> Name: {e1.name}, ID: {e1.emp_id}")
