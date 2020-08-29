#Sample input: abracadabra
#              5 k
#SAmple output:abrackdabra

def mutate_string(string, position, character):
    mylist = list(string)
    mylist[position] = character
    
    newStr = ""
    for i in mylist:
        newStr = newStr+i
    return  newStr

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
