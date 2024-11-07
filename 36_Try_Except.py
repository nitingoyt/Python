# try and except method to use in exception handling



try:
    a = int(input("Enter a number: "))
    for i in range(1,12):
        if(i<=10):
            mul = a*i
            print(f"{a} X {i} = {mul}")
    b = (2, "jaat")
    print(b[3])
# except ValueError as e:
#     print("Entered value is invalid")

# except  IndexError as e:
#     print("Invalid Index")

except Exception as e:
    print(e)


