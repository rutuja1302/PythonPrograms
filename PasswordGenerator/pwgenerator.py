#Password Generator program
#i/p - length of the password
#o/p - Password generated

import random

print("<...WELCOME TO YOUR PASSWORD GENERATOR...> \n")
#read the length 
len_pw = int(input("Enter the desired length for your password: "))

#create a list of characters
char_list = ["A","b","c","d","E","f","g","h","i","J","k","l","m","n","O","p","q","R","s","t","u","v","W","x","y","Z","1","2","3","4","5","6","7","8","9","!","@","#","$","%"]

#Create an empty string for output
resStr = ""

for i in range(0,len_pw):
    index = random.randrange(0,len(char_list)+1)
    resStr += char_list[index]

#Display output
print("Your Generated Secure Password is: "+resStr)
