# multiple inheritance
class fighters_name:
    # name = ""
    def name(self):
        print(self.name)
    

class fighters_batchID():
    # batchID = ""
    def batchID(self):
        print(self.batchID)

       
class Elites(fighters_name, fighters_batchID):
    def info(self):
        print(f"Fighter with ID-{self.batchID} identify by the name of {self.name}")
        
f1 = Elites()
f1.name = "Laila"
f1.batchID = "F1401"
f1.info() 

# multilevel inheritance

class fieldmarshal:
    def __init__(self , fieldmarshalname):
        self.fieldmarshalname = fieldmarshalname
    
class general(fieldmarshal):
    def __init__(self , generalname , fieldmarshalname):
        self.generalname = generalname
        fieldmarshal.__init__(self , fieldmarshalname)

class brigadier(general , fieldmarshal):
    def __init__(self, brigadiername , generalname , fieldmarshalname):
        self.brigadiername = brigadiername
        general.__init__(self , generalname, fieldmarshalname)
  
    def rank(self):
        print(f"ranks orders are:{self.fieldmarshalname} > {self.generalname} > {self.brigadiername}")


r = brigadier("Raj" , "Charlie" , "Nukal")
print(r.fieldmarshalname)
r.rank()


