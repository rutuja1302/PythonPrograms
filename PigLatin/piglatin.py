#Pig Latin program using python
#Logic - User will enter a word/string, if the string starts with vowel then the program will return string+"way"
#If the string starts with a consonent then it will take the first letter, assign it to the back to the word + add "ay"

myStr = input("Enter a String: ").lower()

resStr = ""

mylist = list(myStr)

if myStr[0]=="a" or myStr[0]=="e" or myStr[0]=="i" or myStr[0]=="o" or myStr[0]=="u":
    mylist.append("way")
else:
    temp_char = mylist[0]
    mylist.remove(mylist[0])
    mylist.append(temp_char)
    mylist.append("ay")

resStr = resStr + resStr.join(mylist)

print("Converted String: "+resStr)
