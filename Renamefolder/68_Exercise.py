import os

files = os.listdir("Renamefolder")
i = 12
for file in files:
    if file.endswith(".jpg"):
        print(file)
        os.rename(f"Renamefolder/{file}", f"Renamefolder/{i}.jpg")
        i = i + 1



