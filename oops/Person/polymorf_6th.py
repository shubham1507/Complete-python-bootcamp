class Person():
    def __init__(self, name):
        self.name = name
    def work(self):
        return f"{self.name} is doing general work"
        
class Student(Person):
    def work(self): #overriding
        return f"{self.name } is studying for k8s"
        
class Employee(Person):
    def work(self): #overriding
        return f"{self.name} is working on k8s"
        

# Polymorphism in action
people = [
    Person("Shubham"),
    Student("Amit"),
    Employee("Neha")
]

for person in people:
    print(person.work())  # Same method, different behavior
        
