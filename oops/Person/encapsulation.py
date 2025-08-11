class Person:
    def __init__(self, name, age, salary):
        self.name = name       # Public variable
        self._age = age        # Protected variable (convention)
        self.__salary = salary # Private variable (name-mangled)

    # Getter for salary (read private data)
    def get_salary(self):
        return self.__salary

    # Setter for salary (write private data with validation)
    def set_salary(self, new_salary):
        if new_salary < 0:
            print("❌ Salary cannot be negative!")
        else:
            self.__salary = new_salary
            print("✅ Salary updated successfully")

    # Property for age (getter & setter using @property)
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0:
            print("❌ Age must be positive!")
        else:
            self._age = value
            print("✅ Age updated successfully")


# Create a Person object
p1 = Person("Shubham", 30, 90000)

# Public variable: direct access
print("Name (public):", p1.name)

# Protected variable: can access, but not recommended
print("Age (protected):", p1._age)

# Private variable: ❌ direct access not possible
# print(p1.__salary)  # This will raise AttributeError

# ✅ Access private variable via getter
print("Salary (via getter):", p1.get_salary())

# ✅ Update private variable via setter
p1.set_salary(95000)
print("Updated Salary:", p1.get_salary())

# ❌ Attempt to set negative salary
p1.set_salary(-5000)

# ✅ Use property for age (encapsulation with @property)
p1.age = 35
print("Updated Age (via property):", p1.age)

# ❌ Invalid age
p1.age = -10
