# A Leap Year should be :
# Divisible by 4
# Not Divisible by 100
# If Divisible by 100, then should be divisible by 400

year = int(input("Enter a year: "))

if year>999:
  if year%4==0:
    print("Divisible by 4")
    if year%100!=0:
      print("And Not Divisible by 100")
      print(str(year)+" is a Leap Year")
    elif year%100==0 and year%400==0:
      print("And Divisible by 100")
      print("But also Divisible by 400")
      print(str(year)+" is a Leap year")
    else:
      print("And Not Divisible by 100")
      print(str(year)+" is Not a Leap Year")
  else:
    print("Not divisible by 4")
    print(str(year)+" is Not a Leap Year")
else:
  print("Enter a Valid Year")
