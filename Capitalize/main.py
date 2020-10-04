import math
import os
import random
import re
import sys

def solve(s):
    result = ""
    #split the sentence
    l = s.split(" ")
    for i in range(0,len(l)):
        l[i] = l[i].capitalize()
        result += l[i]+" "
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
