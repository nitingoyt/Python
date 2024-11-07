
class shape:
    def __init__(self , l , b):
        self.l = l 
        self.b = b
    def area(self):
        return self.l * self.b

class circle(shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)
    def area(self):
        return 3.14 * super().area()
           

b = shape(9, 10)
print(b.area())
c = circle(5)
print(c.area())