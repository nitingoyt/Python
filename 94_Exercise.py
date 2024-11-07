# Write a python program which reminds you of drinking water every hour or two. 
# Your program can either beep or send desktop notifications for a specific operating system
import time
from plyer import notification

def reminder_every_2hours():
    while True:
        notification.notify(
            title="Hey !",
            message="Stay Hydrated , bitch!!!!!!!",
            app_name="MyApp",
            timeout=(5)  # Duration in seconds
        )
        time.sleep(2*60*60)

reminder_every_2hours()