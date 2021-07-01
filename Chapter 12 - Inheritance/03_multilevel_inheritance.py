class Person:
    country = "India"
    def takeBreak(self):
        print("Breathing")

class Employee(Person):
    company = "Honda"
    def getSalary(self):
        print(f"Salary {self.salary}")
    def takeBreak(self):
        print("Lol")

class Programmer(Employee):
    company = "Fiverr"
    def getSalary(self):
        print(f"No")

p = Person()
p.takeBreak()
e = Employee()
e.takeBreak()
pr = Programmer()
pr.takeBreak()