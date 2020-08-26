#input - 2
#        1 2

#output - 3713081631934410656

n = int(input())
mylist = list(map(int, input().split()))
t = tuple((mylist))
print(hash(t))
