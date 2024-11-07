# string methods of upper() lower() strip() etc
name = " binod kumar"

birth = "$$$$India$$$$"

print(name.upper())

print(name.lower())
# strips any white spaces from string
print(name.strip())

print(birth.rstrip("$$"))

print(name.replace("kumar", "Yadav"))

print(name.split(" "))

intro = "this is an Introduction"
print(intro.capitalize())

print(intro.center(100, ">"))

print(intro.count("i"))

print(intro.endswith("ion"))

str2 = "World kill a mocking bird"
print(str2.istitle())

print(str2.title())

