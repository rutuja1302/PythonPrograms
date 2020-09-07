# Program - Prime Number
#I/p - Integer number  
#o/p - Prime or not

myNum = int(input("Enter a number "))

count = 0;

for i in range(1,myNum+1):
    if myNum%i == 0:
        count += 1

if count==2:
    print("Prime Number")
else:
    print("Not a Prime Number")
