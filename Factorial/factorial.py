#read the input
num = int(input("Enter a number: "))
#initialise a variable to store result
res = 1
#Factorial for 0 & 1 is 1
#Factorial for negative number doesnot exists
#Factorial of a number(greater than 1) multiplies that number by every number below it

if num == 0:
  print("Factorial of 0 is 1")
elif num == 1:
  print("Factorial of 1 is 1")
elif num < 0:
  print("Factorial doesnot exists")
elif num > 1:
  while num >= 1:
    res = res*num
    num -= 1
  else:
    print("Factorial of number is ",res)
