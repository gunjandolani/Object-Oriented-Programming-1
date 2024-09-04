class parrot:
    def __init__(self , name , color , age):
        self.name = name
        self.color = color
        self.age = age

    def PrintAllDetails(self):
        print("Name:" , self.name)
        print("Color:" , self.color)
        print("Age:" , self.age)

    def PrintName(self):
        print("Name:" , self.name)

    def PrintAge(self):
        print("Age:" , self.age)

    def PrintColor(self):
        print("Color:" , self.color)


parrot1 = parrot("Coco" , "White" , 3)
parrot1.PrintAllDetails()
parrot1.PrintName()
parrot1.PrintAge()
parrot1.PrintColor()
