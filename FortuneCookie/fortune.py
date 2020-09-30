#Fortune teller program 
import random 

#list of fortunes
fortune = ["Constant grinding can turn an iron rod into a needle.",
           "Hearty laughter is a goodway to jog internally without having to go outdoors.",
           "If you want the rainbow, you have to tolerate the rain.",
           "A lifetime of happiness lies ahead of you!",
           "All things are difficult before they are easy.",
           "The current year will bring you much happiness!",
           "Where your treasure is, there will your heart be also <3",
           "You have strong potential for financial success!",
           "Correction does much, but encouragement is everything!",
           "Any day above ground is a good day.",
           "Today is your day!",
           "Smile and know that you are loved :)",
           "Be a Gamechanger, the world has enough followers.",
           "You are amazing just the way you are!",
           "A goal without a plan is just a wish!",
           "Never Give Up, Never Give In!",
           "I hope today is a great day for you!",
           "Doubt kills dreams than failure ever will!"
          ]

#length of the list
l = len(fortune)

#generate a random number
myNum = random.randrange(0,l+1)
#print the result
print("WELCOME TO YOUR PYTHON FORTUNE TELLER!")
print(".........")
print("Your Fortune Cookie Says: ")
print()
print(fortune[myNum])
