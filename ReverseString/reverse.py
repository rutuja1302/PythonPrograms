#Reverse a string

#read a string
myString = str(input("Enter a string: "))

#In python, Strings are arrays
#To acccess an element of a string just access by specifying the index of the character

#index starts from 0 and ends at length - 1
#initializing end index
size = len(myString) - 1

print()
print("Your Reverse String: ")

#looping to get reverse string 
while size>=0:
  print(myString[size],end="")  #end="" will ensure that the string gets printed on one line
  size -= 1
