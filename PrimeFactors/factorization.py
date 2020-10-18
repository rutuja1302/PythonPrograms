#Prime Factorization Program
# This program will read an integer as an input
# Calculate it's prime factors (Prime factors: 2,3,5,7,11...)
#Return the result

import math

def primeFactors(n):
   l = []
   while n % 2 == 0:
      l.append(2),
      n = n / 2
  
   for i in range(3,int(math.sqrt(n))+1,2):
     
      while n % i== 0:
         l.append(i)
         n = n / i
   
   if n > 2:
      l.append(i)

   print(l)

n = int(input("Enter the Number to Factor: "))
primeFactors(n)
