class Employee:
    company = "google"

    def getSalary(self):
        print(f"salary {self.company} is {self.salary}")

    @staticmethod
    def greet():
        print("GM")

harry = Employee()
# harry.salary = 10000000000
# harry.getSalary() # Employee.getSalary(harry)
harry.greet() # Employee.greet()