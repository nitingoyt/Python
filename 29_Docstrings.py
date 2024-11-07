# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.
# PEP stands for Python Enhancement Proposal, and there are several of them. 
# A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.
import numbers
import this
def cube1(a):
    '''takes value of a and returns cube of a'''
    print("Cube of", a, ": ", pow(a, 3))

a = int(input("Enter the number: "))
cube1(a)
print(cube1.__doc__)