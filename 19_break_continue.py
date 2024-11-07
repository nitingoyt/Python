# use of break and continue statements

for i in range(1,5,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")


i = 0
while True:
  print(i)
  i = i + 1
  if(i%10 == 0):
    break