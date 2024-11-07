
class death:
    Name = "Alpha"
    Cause = "Murder"
    def info(self):  
        print(f"Soldier {self.Name} , cause of death is {self.Cause}")

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It must be provided as the extra parameter inside the method definition.

a = death()
b = death()

a.Name = "Romeo"
a.Cause = "On Feild"

b.Name = "Bravo"
b.Cause = "Landmine"

a.info()
b.info()