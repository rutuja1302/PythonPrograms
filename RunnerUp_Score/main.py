#Runner-Up Score problem

#reads n - the length of list
n = int(input("Enter n: "))

#reads scores
scores = map(int, input("Enter scores: ").split())

#Converting scores object to a list by iterating throught the scores
mylist = list()
myiter = iter(scores)
while n!= 0:
  x = next(myiter)
  mylist.append(x)
  n -= 1

#sorting the list
mylist.sort()

#removing the highest score so that we get the runner up score
x = max(mylist)
count_max = mylist.count(x)  #because the highest score can be repeated twice/thrice in a list
while count_max != 0:
  mylist.remove(x)
  count_max -= 1
  
#Printing the runner up score
print("Runner-Up Score: ",max(mylist))
