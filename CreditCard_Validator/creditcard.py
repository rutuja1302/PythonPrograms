#Credit card validator

#read input
card_num = int(input("Enter a credit card number: "))
copy_num = str(card_num)

#length of the number should be 16 else it is invalid
if len(copy_num) == 16:
    set1 = []
    set2 = []
    #separate even placed & odd placed numbers in 2 sets
    for i in range(0,16):
        if i%2==0:
            set1.append(copy_num[i])
        else:
            set2.append(copy_num[i])
    #count number of digits grater than 4 in set1
    count = 0
    for i in range(0,8):
        if int(set1[i]) > 4:
            count += 1
    #Add all the digits of set1 and multiply the result by 2
    sum1 = 0
    for i in range(0,8):
        sum1 += int(set1[i])
    sum1 *= 2
    #Add all the digits of set2
    sum2 = 0
    for i in range(0,8):
        sum2 += int(set2[i])
    #Now add count, sum1 and sum2
    final_res = count + sum1 + sum2
    #if final_res is divisible by 10 then the credit card is valid otherwise not
    if final_res%10==0:
        print("The credit card number is valid!")
    else:
        print("Oops! The credit card number is not valid!")
else:
    print("Invalid Number")

