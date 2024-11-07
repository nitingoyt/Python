# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. 
# Your program should use time module to get the current hour.
import time

time_now = time.strftime('%H: %M: %S')

hour = int(time.strftime('%H'))


if(hour>=5 and hour<12):
    print("Good Morning Sir!")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir!")
elif(hour>=17 and hour<21):
    print("Good Evening Sir!")
else:
    print("Goodbye!")