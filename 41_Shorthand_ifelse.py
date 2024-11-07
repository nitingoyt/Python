# If ... Else in One Line
# There is also a shorthand syntax for the if-else statement that can be used when the condition 
# being tested is simple and the code blocks to be executed are short.

num = int(input("Enter any number: "))

print(num) if num>10 else print("number is too short")


a = 330000
b = 3303
print("A") if a > b else print("=") if a == b else print("B")

c = 9 if a<b else 0
print(c)