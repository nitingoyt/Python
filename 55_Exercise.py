# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent 
# a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. 
# Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. 
# Use proper functions to check for win.
import random

print("""Welcome to the Game! 
SNAKE🐍 WATER💦 GUN🔫"""
    )

print("Choose 1 for 'snake' , 2 for 'water' , 3 for 'gun' and enter 0 to quit")
dict = {'1':"SNAKE🐍",
        '2':"WATER💦", 
        '3':"GUN🔫"
    }

def game(a, b):
    if a==b:
        print("Draw")
    elif (a=='1' and b=='2') or \
         (a=='2' and b=='3') or \
         (a=='3' and b=='1'):
        print("You won")  
    else:
        print("You lose")

while True:
    a = int(input("User Input:"))
    if a==0:
        print("Thanks for playing!")
        break
    if a>3 or a<1:
        print("Invalid input")
        continue
    b = int(random.randint(1, 3))
    b = str(b)
    a = str(a)
    print("AI Input:", b)
    print(f"{dict[a]} vs {dict[b]}") 
    game(a,b)
