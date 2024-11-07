class Animal:
    def __init__(self, name):
        self.name = name
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name)
        self.breed = breed

    def make_sound(self):
        print("Bark!") 

class cat(Animal):
    def __init__(self , name , age):
        Animal.__init__(self, name)
        self.age = age
    
    def make_sound(self):
        print("meowww")
        # return super().make_sound()


c = cat("billi", "22")
c.make_sound()

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Dog")
a.make_sound()

# Quick Quiz: Implement a Cat class by using the animal class. Add some methods specific to cat