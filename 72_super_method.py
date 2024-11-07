
class fighters:
    def __init__(self, name, batchID):
        self.name = "Patel"
        self.batchID = "FI202"
    

class Elites(fighters):
    def __init__(self, name ,batchID, country):
        self.country = country
        super().__init__(name, batchID)

    def info(self):
        print(f"Fighter with ID-{self.batchID} identify by the name of {self.name} belongs to {self.country}")

        

f1 = fighters("Laila","F1401")
f1 = Elites("Laila","F1401","china")
b = f1.info()

# another example
class batch:
    def __init__(self, name , id):
        self.name= name
        self.id = id

class employee(batch):
    def __init__(self, name, id, unitnum):
        self.unitnum = unitnum
        super().__init__(name, id)
    def info(self):
        print(f"Batch container number {self.unitnum} contains life pod of {self.name} with id {self.id}")
    def pas(self):
        return f"Batch container number {self.unitnum} contains life pod of {self.name} with id {self.id}"


a = batch("Raj", "LP101")
a = employee("Rajesh", "LP401", "22")

# a.info()
print(a.pas())


