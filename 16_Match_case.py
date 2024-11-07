# use of match case in python

i = int(input("Enter a Value: "))

match i:
    case 0:
        print("value of i is zero")
    
    case 1:
        print("value if i is 1")
    
    case 2 if(i==100):
        print("value i is 100")
    
    case _:
        print(i)