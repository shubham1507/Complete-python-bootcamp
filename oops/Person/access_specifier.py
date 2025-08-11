class Person:
    # Public class variable
    species = "Homo sapiens"

    def __init__(self, name, age, salary):
        # Public instance variable
        self.name = name
        
        # Protected instance variable (by convention)
        self._age = age
        
        # Private instance variable (name-mangled)
        self.__salary = salary

    # Public method
    def public_method(self):
        return f"Public Method: Name is {self.name}"

    # Protected method
    def _protected_method(self):
        return f"Protected Method: Age is {self._age}"

    # Private method
    def __private_method(self):
        return f"Private Method: Salary is {self.__salary}"

    # Public method that accesses private method internally
    def access_private_method(self):
        return self.__private_method()


# Create object
p1 = Person("Shubham", 30, 90000)

# --- Accessing Public Members ---
print("Public variable:", p1.name)
print(p1.public_method())

# --- Accessing Protected Members (possible but discouraged) ---
print("\nProtected variable (direct access):", p1._age)
print(p1._protected_method())

# --- Accessing Private Members ---
# print(p1.__salary)       # ❌ AttributeError: not directly accessible
# print(p1.__private_method())  # ❌ AttributeError

# Correct way: via public method inside class
print("\nPrivate variable via name-mangling:", p1._Person__salary)  # name-mangled access
print("Private method via public wrapper:", p1.access_private_method())
