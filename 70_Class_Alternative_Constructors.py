

class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    @classmethod
    def fromstring(cls , string):
        return cls(string.split("-")[0], string.split("-")[1])
    
a1 = person("Nitin", "19")
string = "Rjesh-19"
a1 = person(string.split("-")[0], string.split("-")[1])
print(a1.name)
print(a1.age)

a2 = person.fromstring(string)
print(a2.name)
print(a2.age)