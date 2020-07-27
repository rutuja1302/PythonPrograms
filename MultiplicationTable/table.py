#Multiplication table 

num = int(input("Enter a number: "))
for i in range(1,11):
    ans = num*i
    str = "{} x {} = {}" #because we cannot concatenate str and int 
    print(str.format(num,i,ans))
