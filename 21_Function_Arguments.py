# Types of arguments
# Default Arguments
# Keyword Arguments
# Variable length Arguments
# Required Arguments

def greet(name , message="RAM RAM"):
    print(message, name)

greet("nitin", "hi")

# 2 keyword

def greet(name, message):
    print(message, name)

greet(message="Good morning", name="Jatt")

# ** variable length
def print_details(**info):
        print(info["name"], info["age"], info["city"])

print_details(name="Rjesh\n", age=30,  city="\nNew York")
