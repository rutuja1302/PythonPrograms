#Flip Coin Problem

#import random class 
import random

#reads input
num = int(input("Number of times to flip a coin: "))

#initialize heads and tails
heads = 0
tails = 0

#ensure user enters positive integer
if num>0:
  for i in range(num):
    #use random function to get value between 1 to 10
    flip = random.randrange(1,11)
    #if value<5 then tails or else heads
    if flip<5:
      tails += 1
    else:
      heads += 1
  #Calculate percentage
  percentHeads = heads/num * 100
  percentTails = tails/num * 100
  
  #print results
  print("Probablity of getting heads: "+str(percentHeads)+"%")
  print("Probablity of getting tails: "+str(percentTails)+"%")
else:
  print("Invalid Number! Enter a valid number")
