#Consider a list (list = []). You can perform the following commands:

#insert i e: Insert integer  at position .
#print: Print the list.
#remove e: Delete the first occurrence of integer .
#append e: Insert integer  at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.

N = int(input())
mylist = list()

for i in range(1,N+1):
  x = list(map(str, input().split()))
  
  if len(x) == 3:
    a = x[1]
    b = x[2]
    
  if len(x) == 2:
    a = x[1]
    
  if x[0] == "insert":
    mylist.insert(a,b)
  elif x[0] == "print":
    print(mylist)
  elif x[0] == "remove":
    mylist.remove(a)
  elif x[0] == "append":
    mylist.append(a)
  elif x[0] == "sort":
    mylist.sort()
  elif x[0] == "pop":
    mylist.pop
  elif x[0] == "reverse":
    mylist.reverse()
