#Swap case program will change upper case letter to lower case & vice versa
# python has a inbuilt string method to swap cases called swapcase()

def swap_case(s):
    res = s.swapcase()
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
