#HANG MAN GAME

import random

#the hanging man function
#hanging man increasing every time the count variable is increased
def punishment(count,to_guess):
    print("Wrong Guess!Try Again!")
    if count== 6:
        print("GAME OVER! COMPUTER WON :(")
        print("The word was: "+to_guess)
        print("   _______")
        print("  |      _|_")
        print("  |     /   \\")
        print("  |     |   |")
        print("  |     \\_ _/")
        print("  |      _|_ ")
        print("  |     / | \\")
        print("  |      / \\")
        print("  |     /   \\")
        print("__|__")

    if count== 5:
        
        print("Only 1 try remaining!")
        print("   _______")
        print("  |      _|_")
        print("  |     /   \\")
        print("  |     |   |")
        print("  |     \\_ _/")
        print("  |      _|_ ")
        print("  |     / | \\")
        print("  |")
        print("  |")
        print("__|__")

    if count== 4:
        
        print("Only 2 tries remaining!")
        print("   _______")
        print("  |      _|_")
        print("  |     /   \\")
        print("  |     |   |")
        print("  |     \\_ _/")
        print("  |       | ")
        print("  |")
        print("  |")
        print("  |")
        print("__|__")

    if count== 3:
        
        print("Only 3 tries remaining!")
        print("   _______")
        print("  |      _|_")
        print("  |     /   \\")
        print("  |     |   |")
        print("  |     \\_ _/")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("__|__")

    if count== 2:
        
        print("Only 4 tries remaining!")
        print("   _______")
        print("  |       |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("__|__")

    if count== 1:
        
        print("Only 5 tries remaining!")
        print("   ")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("__|__")

#list of possible words for the game
words = ["absurd","avenue","jockey","luxury","oxygen","subway",
         "zombie","burger","cookie","donkey","scared","wealth","vessel"]
#String guess for user display
guess = "******"
l = list(guess)
op_str = ""
#initializing points and count variable
points = 0
count = 0
#Welcome statement & game rules
print("WELCOME TO THE HANGMAN GAME")
print()
print("Rules of the game: ")
print("1» 6 letterd word will be given to you.")
print("2» You have total 6 tries to guess the word right!")
print("3» With each correct guess computer fills in the spaces & you earn points")
print("4» If you guess the word right, YOU WIN! Else the COMPUTER WINS!")
print()
print("......Let's Begin......")

#display the guess string to the user
print("Guess the word: "+guess)
#picks any random word from the list
to_guess = str(words[random.randrange(0,len(words))])

#Six tries given to the user by using for loop
for i in range(1,7):
    user_guess = input("Enter a letter you think would be a better fit: ").lower()
    index = to_guess.find(user_guess)
    if index>=0:
        points += 10
        l[index] = user_guess
        print("Correct Guess! Now your word becomes: "+op_str.join(l))
        print("Your points » "+str(points))
    else:
        count += 1
        punishment(count,to_guess)
        
if points==60:
    print("Congratulations!You have won!")
else:
    print("Oops! Time out,You had only 6 tries!")
    print("The word was: "+to_guess)
