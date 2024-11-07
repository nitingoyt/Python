import shutil
import os

# shutil.copy("example.txt" , "newexample.txt")
# os.remove("newexample.txt")

# shutil.copytree("Renamefolder" , "pythoncopy")
# os.remove("pythoncopy")


# shutil.move('example1.txt' , 'Renamefolder\exae.txt')


# Ensure the source file exists
with open('example.txt', 'w') as f:
    f.write("This is a source file.")

# Copy the file
shutil.copy('example.txt', 'examplecopy.txt')

# Move the file
shutil.move('examplecopy.txt', 'move_examplecopy.txt')

# Create a directory and move the file into it
os.makedirs('new_directory', exist_ok=True)
shutil.move('move_examplecopy.txt', 'new_directory/moved_examplecopy.txt')

# Remove the directory and its contents
shutil.rmtree('new_directory')
