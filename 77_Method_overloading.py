
class vectors:
    def __init__(self, i, j, k):
        self.i = i        
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self, x):
        return vectors((self.i + x.i) , (self.j + x.j) , (self.k + x.k))
    
    
z = vectors(2, 3, 5)
x = vectors(2, 8, 4)
print(x+z)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"



point1 = Point(2, 3)
point2 = Point(4, 5)


print(point1 + point2) 
print(point1 - point2)  
print(point1 * point2) 
print(point1 / point2) 
