'''Write a program to return the difference between the largest and smallest numbers from an array of positive integers.
Note:
You are expected to write a code in the findLargeSmallDifference function only which will receive the first parameter as the number items in the array and second parameter as the array itself.
You are not required to take input from the console.

Example:
Finding the difference between the largest and smallest from a list of 5 numbers
Input
Input 1: 5
Input 2: 10 11 7 12 14
Output
7
'''

#function to calculate difference between the largest and smallest from a list
def findLargeSmallDifference(n,l):
    large = max(l)
    small = min(l)
    difference = large - small
    return difference

#read inputs
n = int(input("Input 1: ")) #size of array
l = list(map(int,input("Input 2: ").split())) #array to hold elements

#driver code
result = findLargeSmallDifference(n,l)
print(result)
