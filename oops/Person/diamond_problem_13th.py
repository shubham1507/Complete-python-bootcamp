class Person:
    def __init__(self, name, **kwargs):
        print("Person.__init__")
        self.name = name
        super().__init__(**kwargs)   # important for cooperative MI

class Employee(Person):
    def __init__(self, emp_id, **kwargs):
        print("Employee.__init__")
        self.emp_id = emp_id
        super().__init__(**kwargs)

class Student(Person):
    def __init__(self, roll_no, **kwargs):
        print("Student.__init__")
        self.roll_no = roll_no
        super().__init__(**kwargs)

# Diamond head: inherits from both Employee and Student
class Voter(Employee, Student):
    def __init__(self, voter_id, **kwargs):
        print("Voter.__init__")
        self.voter_id = voter_id
        super().__init__(**kwargs)

v = Voter(
    voter_id="V34542e",
    emp_id=45429656,
    roll_no=31,
    name="Shubham"
)

print("\nFinal object:", v.name, v.emp_id, v.roll_no, v.voter_id)
print("MRO:", [c.__name__ for c in Voter.mro()])
