class Person:
    def __init__(self, name):
        self.name =  name
    def work(self):
        return f"{self.name} is working.."
        
class Student:
    def __init__(self, name):
        self.name = name
    def work(self):
        return f"{self.name} is studying.."
        
class Robot:
    def __init__(self, id):
        self.id = id
    def work(self):
        return f"{self.id} is processing data"
        
def perform_work(entity):
    # here we dont check class just call method
    print(entity.work())
    
p1 = Person("Shubham")
s1 = Student("Amit")
r1 = Robot("RX-101")

perform_work(p1)  # Person's work()
perform_work(s1)  # Student's work()
perform_work(r1)  # Robot's work()
