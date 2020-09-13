#Harmonic Number
#Logic - H1 = 1
#        H2 = H1 + 1/2
#        H3 = H2 + 1/3         
#        Hn = Hn-1 + 1/n

#read input n
n = int(input("Enter a number: "))

#initializing hn(harmonic number)
hn = 1

#ensuring n!=0
if n!=0:
    for i in range(2,n+1):
        hn = hn + 1/i

    print("Harmonic value for "+str(n)+" is:")
    print(hn)
else:
    raise Exception("Invalid Number")
