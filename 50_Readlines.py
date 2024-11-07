
f = open("example.txt", 'r')
i=0
while True:
    i = i+1
    lines = f.readline()
    if not lines:
        break    
    l0 = lines.split(", ")[0]
    l1= lines.split(", ")[1]
    l2 = lines.split(", ")[2]
    print(f"Marks of student {i} in English :{l0}")
    print(f"Marks of student {i} in MAths :{l1}")
    print(f"Marks of student {i} in Bio :{l2}")

print(lines)

f = open('example.txt', 'w')
lines = ['50,98,77\n', '59\n', '38\n']
f.writelines(lines)
f.close()

f = open("example.txt", 'r')
content = f.read()
print(content)



