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
        print("Result: "+str(result)+"°F")
    elif u1=="fahrenheit" and u2=="celcius":
        #Fahrenheit to Celcius -> (0°F − 32) × 5/9 = -17.78°C
        result = (value-32)*0.556
        print("Result: "+str(result)+"°C")
    elif u1=="celcius" and u2=="kelvin":
        #Celcius to Kelvin -> 0°C + 273.15 = 273.15K
        result = value + 273.15
        print("Result: "+str(result)+"K")
    elif u1=="kelvin" and u2=="celcius":
        #Kelvin to Celcius -> 0K − 273.15 = -273.1°C
        result = value - 273.15
        print("Result: "+str(result)+"°C")
    elif u1=="kelvin" and u2=="fahrenheit":
        #Kelvin to Fahrenheit -> (0K − 273.15) × 9/5 + 32 = -459.7°F
        result = (value - 273.15) * 1.8 + 32
        print("Result: "+str(result)+"°F")
    elif u1=="fahrenheit" and u2=="kelvin":
        #Fahrenheit to Kelvin -> (0°F − 32) × 5/9 + 273.15 = 255.372K
        result = (value - 32) * 0.556 + 273.15
        print("Result: "+str(result)+"K")

#function to convert length units
def length(u1,u2,value):
    #Units : Kilometre;Metre;Centimetre;Millimetre;Foot;Inch

    if u1 =="kilometre" and u2 == "metre":
        #Kilometre to Metre -> multiply the length value by 1000
        result = value * 1000
        print("Result: "+str(result)+"m")
    elif u1 == "metre" and u2 == "kilometre":
        #Metre to Kilometre -> divide the length value by 1000
        result = value / 1000
        print("Result: "+str(result)+"Km")
    elif u1 == "centimetre" and u2 == "metre":
        #Centimetre to Metre -> divide the length value by 1000
        result = value / 1000
        print("Result: "+str(result)+"m")
    elif u1 == "millimetre" and u2 == "centimetre":
        #Millimetre to Centimetre -> divide the length value by 10
        result = value/10
        print("Result: "+str(result)+"cm")
    elif u1 == "foot" and u2 == "inch":
        #Foot to Inch -> multiply the length value by 12
        result = value * 12
        print("Result: "+str(result)+"inch")

#function to convert mass units
def mass(u1,u2,value):
    #Units - Milligram ; Gram ; Kilogram ; Tonne

    if u1 == "milligram" and u2 == "gram":
        # Milligram to Gram -> divide the length value by 1000
        result = value / 1000
        print("Result: "+str(result)+"g")
    elif u1 == "gram" and u2 == "kilogram":
        #Gram to Kilogram -> divide the length value by 1000
        result = value / 1000
        print("Result: "+str(result)+"Kg")
    elif u1 == "kilogram" and u2 == "tonne":
        #Kilogram to Tonne ->divide the length value by 1000
        result = value / 1000
        print("Result: "+str(result)+"tonne")
    elif u1 == "kilogram" and u2 == "gram":
        #Kilogram to Gram -> multiply the length value by 1000
        result = value * 1000
        print("Result: "+str(result)+"g")

#function to convert angle units
def angle(u1,u2,value):
    #Units - Degree;Radian

    if u1 == "degree" and u2 == "radian":
        #Degree to Radian -> 1Deg × π/180 = 0.01745Rad
        result = value * (3.1415/180)
        print("Result: "+str(result)+"Rad")
    elif u1 == "radian" and u2 == "degree":
        #Radian to Degree -> 1Rad × 180/π = 57.296Deg
        result = value * (180/3.1415)
        print("Result: "+str(result)+"Deg")

if unit_type == "temperature":
    temp(unit1,unit2,value)
elif unit_type == "length":
    length(unit1,unit2,value)
elif unit_type == "mass":
    mass(unit1,unit2,value)
elif unit_type == "angle":
    angle(unit1,unit2,value)
else:
    print("Invalid Option")
