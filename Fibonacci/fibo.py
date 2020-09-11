#fabonacci sequence for n numbers

#read n
n = int(input("Enter n: "))

#intialize first, second term & sum
ft = 0
st = 1
sum = 0

#print the sequence
for i in range(0,n):
  sum = ft + sum
  print(sum,end=" ")
  ft = st
  st = sum
