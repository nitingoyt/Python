# Write a program to clear the clutter inside a folder on your computer. 
# You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. 
# Do the same for other file formats. For example:
# sfdsf.png --> 1.png

import os

import os

files = os.listdir("Renamefolder")
i = 12
for file in files:
    if file.endswith(".jpg"):
        print(file)
        os.rename(f"Renamefolder/{file}", f"Renamefolder/{i}.jpg")
        i = i + 1
