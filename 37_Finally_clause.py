# Finally Clause



def nums():
  try:
    l = [2, 4, 59 ,35]
    i = int(input("Enter a inndex: "))
    print(l[i])
    return 1
  except:
    print("Error Occured")
    return 0
  finally:
    print("I am Inevitable")

x = nums()
print(x)