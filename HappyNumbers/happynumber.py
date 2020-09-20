#happy numbers
#a happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit
#For example: 13 is a happy number
# 1^2 + 3^2 = 10 -> 1^2 + 0^2 = 1
#if the result is 1, then happy number & if the result is the number entered itself, then it is a unhappy number

import math

#Read an integer
myNum = int(input("Enter a number: "))
looping_num = myNum
#initialize result
result = 0
#repeat the steps until result is either 1 or the number it self
while result!=1 and result!=myNum:
    myStr = str(looping_num)
    ln = len(myStr)
    result = 0
    for i in range(ln):
        result += int(math.pow(int(myStr[i]),2))
    looping_num = result
else:
    if result==1:
        print(str(myNum)+" is a Happy Number")
    else:
        print(str(myNum)+" is a Unhappy Number")
