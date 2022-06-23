
class Vehicle():
    def __init__(self, type):
        self.type = type

class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    def showDetails(self):
        print(f'||| Vehicle Info |||\nType: {self.type}\nyear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of doors: {self.doors}\nStyle of roof: {self.roof}')

myType = input('Vehicle Type: ') 
myYear = input('Year: ')
myMake = input('Make: ')
myModel = input('Model: ')
myDoors = input('Number of doors: ')
myRoof = input('Style of roof(open/closed): ')
transport = Vehicle(myType, myYear, myMake, myModel, myDoors, myRoof)
transport.showDetails()


 

