#Read encrypted message from user
code = input("Enter your message to encrypt: ")
#convert string into iterable list
l = list(code)

#create a dictionary for all the codes
decrypt = {"+":"a","-":"b","*":"c","/":"d","\'":"e",
        "\"":"f",")":"g","[":"h","{":"i",":":"j",
        "#":"k","?":"l","%":"m","}":"n","$":"o",
        "<":"p","~":"q",";":"r","&":"s","|":"t",
        "€":"u","¥":"v","(":"w","¿":"x",">":"y","]":"z"," ":" "}

#iterate through the list and replace words by codes we assigned
og_msg = ""

for i in range(0,len(l)):
    og_msg += decrypt[l[i]]

#print final result
print("Your Decrypted Message:")
print(og_msg)
