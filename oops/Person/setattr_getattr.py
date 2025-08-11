class Person:
    species = "Homo sapiens"  # Class variable

    def __init__(self, name, age):
        self.name = name      # Public instance variable
        self._age = age       # Protected instance variable
        self.__salary = 0     # Private instance variable

    def display_info(self):
        return f"Name: {self.name}, Age: {self._age}, Species: {Person.species}"


# Create object
p1 = Person("Shubham", 30)

# --- Using setattr() to set attributes dynamically ---
setattr(p1, "name", "Amit")        # Update existing public variable
setattr(p1, "_age", 25)            # Update protected variable
setattr(p1, "_Person__salary", 50000)  # Update private variable (name-mangled)
setattr(p1, "city", "Pune")        # Create a new attribute on the fly

# --- Using getattr() to get attributes dynamically ---
print("Name:", getattr(p1, "name"))
print("Age:", getattr(p1, "_age"))
print("Salary (private):", getattr(p1, "_Person__salary"))
print("City:", getattr(p1, "city"))

# If attribute doesn't exist, provide a default value to avoid error
print("Country:", getattr(p1, "country", "India"))

# Display final info
print("\nFinal Person Info:", p1.display_info())
