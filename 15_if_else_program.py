import time

timeframe = time.strftime('%m, %d, %H, %M ,%S, %p')

print(timeframe)

# program to greet ur teacher specific times of the day

timeframe1 = int(time.strftime('%H'))
timeframe2 = (time.strftime('%p'))

print(timeframe1)
if(5<=timeframe1<12):
    print("Good Morning Sir", timeframe1,timeframe2)
elif(12<=timeframe1<16):
    print("Good Afternoon Sir")
elif(16<=timeframe1<21):
    print("Good Evening Sir")
else:
    print("Goodbye")