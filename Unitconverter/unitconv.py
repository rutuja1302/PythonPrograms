#unit converter program

print("Python Unit Converter")
print("Choose type of unit from the following: 1)Temperature 2)Length 3)Mass 4)Angle")

#read type of unit
unit_type = input("Enter type of unit: ").lower()
#read unit1 type
unit1 = input("From unit: ").lower()
#read unit2 type
unit2 = input("To unit: ").lower()
#read the value for unit 1
value = int(input("Enter Value: "))

#function to convert temperature units
def temp(u1,u2,value):
    #Units- Celcius;Fahrenheit;Kelvin
    
    if u1=="celcius" and u2=="fahrenheit":
        #Celcius to Fahrenheit -> (0°C × 9/5) + 32 = 32°F
        result = (value*1.8)+32
        print(result)
    elif u1=="fahrenheit" and u2=="celcius":
        #Fahrenheit to Celcius -> (0°F − 32) × 5/9 = -17.78°C
        result = (value-32)*0.556
        print(reult)
    elif u1=="celcius" and u2=="kelvin":
        #Celcius to Kelvin -> 0°C + 273.15 = 273.15K
        result = value + 273.15
        print(reult)
    elif u1=="kelvin" and u2=="celcius":
        #Kelvin to Celcius -> 0K − 273.15 = -273.1°C
        result = value - 273.15
        print(reult)
    elif u1=="kelvin" and u2=="fahrenheit":
        #Kelvin to Fahrenheit -> (0K − 273.15) × 9/5 + 32 = -459.7°F
        result = (value - 273.15) * 1.8 + 32
        print(reult)
    elif u1=="fahrenheit" and u2=="kelvin":
        #Fahrenheit to Kelvin -> (0°F − 32) × 5/9 + 273.15 = 255.372K
        result = (value - 32) * 0.556 + 273.15
        print(reult)
    else:
        print("Invalid input")


if unit_type == "temperature":
    temp(unit1,unit2,value)
