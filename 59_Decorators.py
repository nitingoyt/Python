def function_decorator(fst):
    def fx(*args, **kargs):
        print("Hi , welcome ")
        fst(*args, **kargs)
        print("Thanks for the visit")
    return fx
    
@function_decorator
def greet():
    print("This is just a message")

@function_decorator
def sums(a, b):
    add = a+b
    print(add)


greet()
sums(5, 8)

