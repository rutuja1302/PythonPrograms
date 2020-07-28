#game rules - rock beats scissors
#             scissor cuts paper
#             paper beats rock
# 5 points game 
#Player1: user Player2:CPU

import random

player_Points = 0
cpu_Points = 0
print("<===ROCK PAPER SCISSORS===>")
print()

while player_Points<5 or cpu_Points<5:
  playerChoice = str(input("Enter your move: ").upper())

  rand = random.randrange(3)
  choices = ['ROCK','PAPER','SCISSORS']

  cpuChoice = choices[rand]
  print("CPU's move: ",cpuChoice)

  if playerChoice == "ROCK" and cpuChoice == "SCISSORS":
    print("Congratulations! You Win!")
    player_Points += 1
    print("Your points: ",player_Points)
    print("CPU's points: ",cpu_Points)
  elif playerChoice == "ROCK" and cpuChoice == "PAPER":
    print("Oops! CPU wins! :(")
    cpu_Points += 1
    print("Your points: ",player_Points)
    print("CPU's points: ",cpu_Points)
  elif playerChoice == "SCISSORS" and cpuChoice == "ROCK":
    print("Oops! CPU wins! :(")
    cpu_Points += 1
    print("Your points: ",player_Points)
    print("CPU's points: ",cpu_Points)
  elif playerChoice == "PAPER" and cpuChoice == "ROCK":
    print("Congratulations! You Win!")
    player_Points += 1
    print("Your points: ",player_Points)
    print("CPU's points: ",cpu_Points)
  elif playerChoice == "PAPER" and cpuChoice == "SCISSORS":
    print("Oops! CPU wins! :(")
    cpu_Points += 1
    print("Your points: ",player_Points)
    print("CPU's points: ",cpu_Points)
  elif playerChoice == "SCISSORS" and cpuChoice == "PAPER":
    print("Congratulations! You Win!")
    player_Points += 1
    print("Your points: ",player_Points)
    print("CPU's points: ",cpu_Points)
  elif playerChoice == cpuChoice:
    print("It's a Tie!")
    print("No one gets a point")
    print("Your points: ",player_Points)
    print("CPU's points: ",cpu_Points)
  
  if player_Points==5 or cpu_Points==5:
    break


if cpu_Points==5:
  print("CPU WINS! BETTER LUCK NEXT TIME!")
elif player_Points==5:
  print("YOU WIN! CONGRATULATIONS!")
  print("Here's your trophy")
  print(" _______")
  print("(       )")
  print(" (     )")
  print("  (  )")
  print("   --")
  print(" { || }")
  print("   ||")
  print("  ----")
