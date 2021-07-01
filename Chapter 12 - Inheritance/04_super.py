class Person:
    country = "India"
    def __init__(self):
        print("PP")
    def takeBreak(self):
        print("Breathing")

class Employee(Person):
    company = "Honda"
    def __init__(self):
        super().__init__()
        print("Yo")
    def getSalary(self):
        print(f"Salary {self.salary}")
    def takeBreak(self):
        super().takeBreak()
        print("Lol")

class Programmer(Employee):
    company = "Fiverr"
    def __init__(self):
        super().__init__()
        print("Pop")
    def getSalary(self):
        print(f"No")
    def takeBreak(self):
        super().takeBreak()
        print("Crying")

# p = Person()
# p.takeBreak()
# e = Employee()
# e.takeBreak()
pr = Programmer()
# pr.takeBreak()