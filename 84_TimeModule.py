import time

def looper():
     for i in range(4900):
       print(i)


init = (time.time())
looper()
print(time.time() - init) #returns time took to execute for loop

print("sleep starts !!")
time.sleep(1)        #puts a sleep delay in bw 
print("sleep ends !!") 



t = time.localtime()
current_time = time.strftime("%Y-%m-%d %H:%M:%S" , t)
print(current_time)