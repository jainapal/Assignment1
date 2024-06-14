# Write a program that asks the user for their birth year and calculates their
#age.
birthyear=int(input("Enter your birth year:"))
curryear=int(input("enter current year"))
if(curryear<birthyear):
    print("Incorrect year")
else:
    age=curryear-birthyear
print(age)