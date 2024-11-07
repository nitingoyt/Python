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


