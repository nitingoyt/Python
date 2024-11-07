# A lambda function is a small anonymous function without a name
# Lambda functions are often used in situations where a small function is required for a short period of time. 
# They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

def foxi(fx, value):
    return 10 + fx(value) 
    
double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3
value1 = lambda a  : a * a
print(double(5))
print(cube(5))
print(avg(3, 5, 10))
print(value1(7))

print(foxi(lambda a:a * a * a, 2))