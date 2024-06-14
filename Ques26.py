# Write a program in python that checks if a string starts with a given prefix
#or ends with a given suffix.
str=input("Enter string:")
pre=input("Enter prefix:")
sufix=input("Enter suffix:")
if(str.startswith(pre) and str.endswith(sufix)):
    print("Yes string starts and ends with given prefix and suffix")
else :
    print("No string do not starts with or ends with given prefix or suffix")