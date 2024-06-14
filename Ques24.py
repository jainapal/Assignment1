# Write a program that acts as a simple calculator. It should take two
#numbers and an operator (+, -, *, /) as input and print the result.
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
operation=input("Enter operation +,-,*,/ :")
if(operation=="+"):
    print(num1+num2)
elif(operation=="-"):
    print(num1-num2)
elif(operation=="*"):
    print(num1*num2)
elif (operation=="/"):
    print(num1/num2)

