# := walrus operator

# numbers = [1,2,3,4,5,6,7,8]
# while(n := len(numbers)) > 0:
#     print(numbers.pop())


items = list()

# while True:
#     items = input("Itmes is :")
    
#     if items == "quit":
#      break

# # while\foods = list()
while (item := input("What food itmes do you like?: ")) != "quit":
    items.append(item)