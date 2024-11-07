# else can be used with for while loops too

int = (3, 4, 5)
i = 1

for i in range(1,12):
    print(f"5 X {i} = {5*i}")
    if(i==11):
      break
else:
    print("End !!!!!!!!!!!!")


