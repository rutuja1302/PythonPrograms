#Read input
og_msg = input("Enter your message to encrypt: ").lower()
#convert string into iterable list
l = list(og_msg)

#create a dictionary for all the codes
code = {"a":"+","b":"-","c":"*","d":"/","e":"\'",
        "f":"\"","g":")","h":"[","i":"{","j":":",
        "k":"#","l":"?","m":"%","n":"}","o":"$",
        "p":"<","q":"~","r":";","s":"&","t":"|",
        "u":"€","v":"¥","w":"(","x":"¿","y":">","z":"]"," ":" "}

#iterate through the list and replace words by codes we assigned
final_code = ""

for i in range(0,len(l)):
    final_code += code[l[i]]

#print final result
print("Your Encrypted Message:")
print(final_code)
