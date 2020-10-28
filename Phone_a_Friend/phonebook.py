#Sample Input
'''3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry'''
#Sample output
'''sam=99912222
Not found
harry=12299933'''

#Read the integer at the first line
n = int(input())
#Create a dictionary to hold the names and phone numbers
phone_book = {}

#Take input for the phone book i.e, Name and Number
for i in range(0,n):
    name,num = input().split(maxsplit=1)
    phone_book[name] = num


#Take unknown number of queries to search name in the phone book
queries = []
query = "  "
while len(query)>1:
    query = input()
    queries.append(query)
queries.pop()

#Search the queries and print the result 
for i in range(0,len(queries)):
    if queries[i] in phone_book.keys():
        print(queries[i]+"="+str(phone_book[queries[i]]))
    else:
        print("Not found")
