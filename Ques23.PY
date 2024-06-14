# Write a program that converts temperature from Celsius to Fahrenheit
#and vice versa based on user input.
temp=float(input("Enter temp:" ))
c=int(input("Enter 1 to convert to celsius and 2 to convert to Fahrenheit"))
if(c==1):
    celsius=(temp - 32) * (5/9)
    print("Temp given in fahrenheit is:",temp)
    print("Temp in celsius is:",celsius)
if(c==2):
    fahrenheit=(temp * (9/5)) + 32
    print("Temp given in celsius is:",temp)
    print("Temp in fahrenheit is:", fahrenheit)