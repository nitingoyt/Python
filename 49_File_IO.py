# FILE READING

# f = open("myname.txt", 'r')
# print(f)
# f.close()


# FILE WRITING
lines  = ["A STAR0\n", "WITH HER\n", "JUST A PEBBLE\n"]
f = open("myname.txt", 'w')
f.write("Argghhhhhhhhhh Shit !!!!\n")
f.writelines(lines)
f = f.close()

# FILE APPEND METHOD
with open("myname.txt", 'a') as f:
    f.write("Last iteration\n")



with open("myname.txt", 'r') as f:
    content = f.read()
    print(content)

# READING A BINARY FILE SUCH AS(JPEG) USING 'b' WITH READ KEYWORD 'r'
with open("d7e5d39850da44e98732efca.jpeg", 'rb') as f:
    con = f.read()
    print(con)
    