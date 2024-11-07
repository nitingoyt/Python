# Write a program to pronounce list of names using win32 API. If you are given a list l as follows:
import win32com.client
import pyttsx3

speaker = win32com.client.Dispatch("SAPI.SpVoice") 
  
list = ["Rahul", "Nishant", "Harry"]
for name in list:
   speak = print(f"Shoutout to {name}")
   speaker.Speak(f"Shoutout to {name}") 

# Another Method
engine = pyttsx3.init()     
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)  

for name in list:
   speak = print(f"Shoutout to {name}")
   engine.say(f"Shoutout to {name}")
   engine.runAndWait()
