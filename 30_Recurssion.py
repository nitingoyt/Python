# Use of recurssion to call functions again and again

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)



# program to print fibbonachi serires of numberes

def fibonacci(m):
    if(m==0):
        return 0
    elif(m==1):
        return 1
    else:
        return fibonacci(m-1)+fibonacci(m-2)

m = int(input("Enter the num: "))

print(fibonacci(m))