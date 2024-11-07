# part 2 of set methods

set_a = {"Stone", "Ring", "Watch", "Heart", "Food"}
set_b = {"Chain", "Keychain", "Watch", "Stone"}

set1 = {1, 2, 3, 4, 5, 7, 8, 6}
set2 = {4, 5, 6, 7, 8}

# isdisjoint 
print(set1.isdisjoint(set2))

# issuperset
print(set1.issuperset(set2))

# issubset
print(set2.issubset(set1))

# add and update

set_a.add("Feelings")
print(set_a)

set1.update(set2)
print(set1)

# remove/discard ->The main difference between remove and discard is that, 
# if we try to delete an item which is not present in set, then remove() raises an error, 
# whereas discard() does not raise any error.

set_a.remove("Feelings")
set_a.discard("")
print(set_a)

# pop() -> This method removes the last item
set1.pop()
print(set2)


# clear(): This method clears all items in the set and prints an empty set.
# del ->del is not a method, rather it is a keyword which deletes the set entirely.



if "Stone" in set_a:
    print("Stone is present")
else:
    print("invalid")