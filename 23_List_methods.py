# List Methods
# append()	Adds an item to the end of the list	list.append(3)
# extend()	Adds all elements of an iterable to the end of the list	list.extend([3, 4])
# insert()	Inserts an item at a specified position	list.insert(1, 'a')
# remove()	Removes the first occurrence of a specified item	list.remove('a')
# pop()	Removes and returns the item at the specified index	list.pop(1)
# clear()	Removes all items from the list	list.clear()
# index()	Returns the index of the first occurrence of a value	list.index('a')
# count()	Returns the number of occurrences of a value	list.count('a')
# sort()	Sorts the list in ascending or descending order	list.sort()
# reverse()	Reverses the order of the list	list.reverse()
# copy()	Returns a shallow copy of the list	new_list = list.copy()
# join()	Concatenates list elements into a string (for strings)	'-'.join(['a', 'b'])

listveges = [ "Apple", "Banana", "Pizza","Sushi","Coffee","Smartphone","Laptop","Smartwatch","Camera","Bluetooth Speaker"]

listnums = [34, 66, 23, 89, 1, 8, 23, 4, 87]

# sort items

listveges.sort()
listnums.sort(reverse=True)

print(listveges)
print(listnums)

# reverse() items

listnums.reverse()

# index() ->This method returns the index of the first occurrence of the list item.

print(listveges.index("Banana"))
print(listnums.index(23))

# count()

print(listveges.count("Camera"))
print(listnums.count(23))

# copy()

newlistnums = listnums.copy()

print(newlistnums)


# append(): This method appends items to the end of the existing list.

newlistnums.append(23)

print(newlistnums)

# insert()

listveges.insert(2, "Mangos")
print(listveges)

# Extend()

listnums1 = [1,2,3,4]
listnums1.extend(listnums)
print(listnums1)