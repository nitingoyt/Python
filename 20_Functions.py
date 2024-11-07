# use of functions in python
import numbers
def pythagrestheorem(a, b, c):
    if(a**2 + b**2 == c**2):
        print("A Right angled traingle for :", a**2 + b**2 == c**2)
        print(a**2, "+", b**2, "==", c**2)
    else:
        print("Not a Right angle traingle")


a = int(input("Enter perpendicular of traingle: "))
b = int(input("Enter base of traingle: "))
c = int(input("Enter Hypotenuse of traingle: "))

pythagrestheorem(a,b,c)