# what are list nd how to use them

ranks =["conquer", "ace", "crown", "diamond"]

print(ranks)

grocery = ["juice", "rice", "pulses", "vegetables", 3, 35, "medicine"]

print(grocery[2])
print(grocery[5])
print(grocery[-2])
print(grocery[0:7:2])

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)