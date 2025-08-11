class Person:
    # class var shared by all
    species = "Home sapies" # class var
    
    def __init__(self, name, age):
        self.name = name # instannce var
        self.age = age # instance var
        
p1 = Person("Shubham", 42)
print(p1.name)
p2 = Person("Amit", 44) # created another object

#instance  var
print(f"p1 is {p1.age} yrs old with name {p1.name}")
print("similarly")
print(f"p2 is {p2.age} yrs old with name {p2.name}")

# class var same for all
print(f"p1 is {p1.species}")

print("similarly")

print(f"p2 is {p2.species}")

print(f"Person.species is {Person.species}, which is global")

# change class var
Person.species = "Human"

print("changed species as Human Now")
print(f"p1 is {p1.species} and p2 is {p2.species}/ but if I change instance vr")
p1.age=34

print(f"age of p1 {p1.age} and p2 {p2.age}")

# covered class object,instance vr and class vr





