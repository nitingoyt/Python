
x = 69

def num():
    x = 70
    global y  # now can be used outside of function too
    y = 55
    print(f"This is local variable {x}")


num()
print(y) # result in error cause y is not defined outside of function
print(f"This is global variable {x}")