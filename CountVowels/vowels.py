#count vowels in a string 
#good news for you is the python already has a function call count() in strings
#so we are just going to implement that

#read a string
st = input("Enter a string: ")

#lower case all the characters as the function is case sensitive
st = st.lower()

#count all the vowels and add them
countVowels = st.count('a') + st.count('e') + st.count('i') + st.count('o') + st.count('u')

#print the result
print()
print("Number of vowels in the string: ")
print(countVowels)
