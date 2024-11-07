# set methods and operations

set_a = {"Stone", "Ring", "Watch", "Heart", "Food"}
set_b = {"Chain", "Keychain", "Watch", "Stone"}

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# # union 

set_c = set_a.union(set_b)
set3  = set1.union(set2)
print(set_c, "\n", set3)

# # update
set_a.update(set1)
print(set_a)

# # intersection && intersection_update
set_c = set_a.intersection(set_b)
print(set_c)

set1.intersection_update(set2)
print(set1)

# symmetric_difference and symmetric_difference_update():

set_c = set_a.symmetric_difference(set_b)
print(set_c)

set1.symmetric_difference_update(set2)
print(set1)