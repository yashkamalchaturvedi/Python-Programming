class Employee:
    company = "Google"

    def showDetails(self):
        print("Employee")

class Programmer(Employee):
    language = "Python"
    def getLanguage(self):
        print(f"language {self.language}")
    def showDetails(self):
        print("Programmer")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)