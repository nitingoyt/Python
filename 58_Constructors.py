# A constructor is a special method in a class used to create and initialize an object of a class.
# There are different types of constructors. Constructor is invoked automatically when an object of a class is created.
# It cannot return any value other than None.

class accounts:
    def __init__(self, n,p):
        print("This is none")
        self.name = n
        self.salary = p
    def info(self):
        print(f"{self.name} earns a salary of {self.salary}")
        

a = accounts("Rajneesh", "12000")
a.info()