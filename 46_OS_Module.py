# # The os module in Python provides a way of interacting with the operating system

import os 

def example_os_operations():
    # Create a new directory
    os.makedirs('example_dir/sub_dir', exist_ok=True)
    print("Directories created.")

    # Change current working directory
    os.chdir('example_dir')
    print(f"Changed working directory to {os.getcwd()}")

    # Create a file
    with open('sub_dir/example.txt', 'w') as file:
        file.write("Hello, world!")

    # List files in sub_dir
    files = os.listdir('sub_dir')
    print(f"Files in 'sub_dir': {files}")

    # Get absolute path of the file
    abs_path = os.path.abspath('sub_dir/example.txt')
    print(f"Absolute path: {abs_path}")

    # Check if the path is a file
    print(f"Is 'example.txt' a file? {os.path.isfile('sub_dir/example.txt')}")

    # Rename the file
    os.rename('sub_dir/example.txt', 'sub_dir/example_renamed.txt')
    print("File renamed.")

    # Remove the file
    os.remove('sub_dir/example_renamed.txt')
    print("File removed.")

    # Remove directories
    os.removedirs('sub_dir')
    print("Directories removed.")

if __name__ == "__main__":
    example_os_operations()
