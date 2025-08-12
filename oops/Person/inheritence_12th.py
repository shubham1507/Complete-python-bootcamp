class Person:
    def __init__(self, name):
        self.name = name
    def show_name(self):
        return f"Name: {self.name}"
        
class Employee(Person): #Single Inheritance
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id
            
    def show_employee(self):
        return f"{self.show_name()}, employee_id: {self.emp_id }"
        
e1 = Employee("Shubham", 45429656)

print("Employee details: ", e1.show_employee())

class Manager(Employee): #Multi-Level Inheritance
    def __init__(self, name, emp_id, dept):
        super().__init__(name, emp_id)
        self.dept = dept
    def show_manager(self):
        return f"Manager: {self.name}, id: {self.emp_id}, dept: {self.dept}"
        
m1 = Manager("Nikhil", 419199, "Devops_IT")

print("My manager details: ", m1.show_manager())

class Skills:
    def __init__(self, skills):
        self.skills = skills
        
class Developer(Person, Skills): #Multiple Inheritance
    def __init__(self, name, skills, emp_id):
        Person.__init__(self, name)
        Skills.__init__(self, skills)
        self.emp_id = emp_id
    def show_dev(self):
        return f"{self.name} is a developer with skills {','.join(self.skills)} with empID as {self.emp_id}"

hsbc = Developer("Shubham",["Python", "DevOps"], 45429656)

print(hsbc.show_dev())

#Multiple children share the same parent.
#Hierarchical Inheritance
class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no =roll_no
        
class Resource(Person):
    def __init__(self, name, billing):
        super().__init__(name)
        self.billing = billing
        
std = Student("sarthak", 21)
it_res = Resource("Shubham", 130000)

print(f"{std.name} is having roll no {std.roll_no} who is brother of {it_res.name} whos monthly salary is {it_res.billing}")

# Hybrid Inheritance
# Combination of more than one type: (Resource -> Person) + Skills

class IT_budget(Resource, Skills):
    def __init__(self, name, billing, skills, budget):
        # Explicitly initialize both bases (consistent with your Developer example)
        Resource.__init__(self, name, billing)   # initializes Person + billing
        Skills.__init__(self, skills)            # initializes skills
        self.budget = budget

    def summary(self):
        return (
            f"Name: {self.name} | Billing: {self.billing} | "
            f"Skills: {', '.join(self.skills)} | Annual IT Budget: ₹{self.budget}"
        )


# Demo
fin = IT_budget("Shubham", 130000, ["Python", "DevOps", "Kubernetes"], 12_00_000)
print(fin.summary())

class Voter(Employee, Student):
    def __init__(self, name, emp_id, roll_no, voter_id):
        Employee.__init__(self, name, emp_id)
        Student.__init__(self, name, roll_no)
        self.voter_id = voter_id

voting_obj = Voter("Shubham", 45429656, 31, "V34542e")

print("\nMRO:", Voter.mro())
