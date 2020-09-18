n,m = map(int, input().split())
width = m
msg = "WELCOME"
design = ".|."
#upper piece
lines = int((n-1)/2)
count = 1
for i in range(1,lines+1):
    a = design*count
    print(a.center(width,'-'))
    count += 2

#center piece
print(msg.center(width,'-'))

#bottom piece
count = n-2
for i in range(1,lines+1):
    a = design*count
    print(a.center(width,'-'))
    count -= 2
