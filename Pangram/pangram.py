#pangram - sentence with all alphabets
#example - The quick brown fox jumps over the lazy dog

#read the input
myStr = input("Enter a sentence: ").lower()

#eliminating all the spaces
myStr = myStr.replace(" ", "")
#eliminating all commonly used special characters
myStr = myStr.replace("," , "")
myStr = myStr.replace("." , "")
myStr = myStr.replace("!" , "")

#converting string to set
#as set only inputs unique values
mySet = set(myStr)

#now, this set should contain all the 26 alphabets
#i.e length of set = 26 then, the str is pangram
if len(mySet) == 26:
    print("Entered string is a Pangram String")
else:
    print("Not a Pangram String")
