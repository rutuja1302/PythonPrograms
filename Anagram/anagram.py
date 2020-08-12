#Anagram Detection 

#reads 2 strings
st1 = input("Enter a string: ")
st2 = input("Enter another string: ")

#check if their lengths are equal
if len(st1) == len(st2):
  #create a list
  n = len(st1)-1
  list1 = list()
  while n >= 0:
    list1.append(st1[n])
    n -= 1
  m = len(st2)-1
  list2 = list()
  while m >= 0:
    list2.append(st2[m])
    m -= 1
  #sort the list
  list1.sort()
  list2.sort()
  #check if lists are equal and print the result
  if list1 == list2:
    print("Anagram")
  else:
    print("Not an anagram")
else:
  print("Not an anagram")
