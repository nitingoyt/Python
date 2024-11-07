
class fighters:
    def __init__(self, name, batchID):
        self.name = "Patel"
        self.batchID = "FI202"
    def info(self):
        print(f"Fighter with ID-{self.batchID} identify by the name of {self.name}")


class Elites(fighters):
    def print(self):
        print(f"belongs to nation")



f1 = Elites("Laila", "F1401")
b = f1.info()
c = f1.print() 

