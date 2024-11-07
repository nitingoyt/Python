# tuple operations
tuple1 = ("murder", "extortion", "kidnapping", "suicide", "homicide", "human_trafficing")

list1 = list(tuple1)
list1.append("killing")
list1.pop(3)
print(list1)

tuple1 = tuple(list1)


class1 = (1, 34, 63)
class2 = (2, 35, 64)

class_all = class1+class2
print(class_all)

# Tuple methods
# index()

print(tuple1.index("kidnapping"))
print(class1.index(34))

# 