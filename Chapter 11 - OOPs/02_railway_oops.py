class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name {self.name}")
        print(f"Train {self.train}")

harrysApplication = RailwayForm()
harrysApplication.name = "Yash"
harrysApplication.train = "Duronto"
harrysApplication.printData()