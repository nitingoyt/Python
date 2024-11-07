# Access Modifier
# public modifer
class general:
    def __init__(self):
        self.name = "raj"  # public variable

a = general()
print(a.name) #public variable accessed


# protected

class private1:
    def __init__(self):
        self.__name = "Buddy" #private variable used (__)

    def __funct(self):    #private function
            self.age = 33
            print(self.age)

class xtraprivate1(private1):
     pass

b = private1()
c = xtraprivate1()
# print(b.__name) #return error 
print(b._private1__name)  #accesed using some method
b._private1__funct()

print(c._private1__name)
c._private1__funct()