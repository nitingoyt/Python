# Map

list1 = [2, 4, 7, 9, 3, 0, 11, 25]

def cube1(x):
    return x*x*x

newlist = (list(map(cube1, list1)))
print(newlist)

# Filter

newnewlist = list(filter(lambda x: x%2==1, list1))
print(newnewlist)

# Reduce 
from functools import reduce

newlist2 = reduce(lambda x , y : (x + y) , list1)


print(newlist2/len(list1))