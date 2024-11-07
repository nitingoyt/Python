#  the seek() and tell() functions are used to work with file objects and their positions within a file. 
# These functions are part of the built-in io module,which provides a consistent interface for reading 
# and writing to various file-like objects, such as files, pipes, and in-memory buffers.

f = open("example.txt", 'r')
f.seek(5)
content = f.read(3)
print(content)

print(f.tell())


with open("example1.txt",'w') as f1:
    f1.write('Why are you reading this !!!!!!')
    f1.truncate(9)

with open('example1.txt','r') as f1:
    content = f1.read()
    print(f1.read())