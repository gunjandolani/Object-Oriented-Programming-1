class Employee:
    def __init__(self , name , designation):
        self.name = name
        self.designation = designation

    def printINFO(self):
        print("Name:" , self.name)
        print("Designation:" , self.designation)

    def printName(self):
         print("Name:" , self.name)
         print("Designation:" , self.designation)


employee1 = Employee("Rajesh" , "Customer Success Engineer")
print(employee1.name)
print(employee1.designation)