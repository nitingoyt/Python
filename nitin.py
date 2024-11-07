import random 
import string
def greet():
    print("welcome sir")
# greet()
print(__name__)
if __name__ == "__main__":
    greet()


if __name__=="__main__":
    print("This runs") 

random_char = random.choice(string.ascii_letters)
print(random_char)

random_alphanum = ''.join(random.choices(string.ascii_letters, k=3))
print(random_alphanum)