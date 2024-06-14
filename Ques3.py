# Write a python program that calculates the factorial of a given number.
Num=int(input("enter number :"))
fact=1
if(Num<0): 
    print("Not a valid number")
else :
    for i in range(1,Num+1):
        fact*=i
    print(fact)  