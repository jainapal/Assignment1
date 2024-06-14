# Write a python program that checks if two strings are anagrams of each
#other.
s1=input("Enter string 1:")
s2=input("Enter string 2:")
if(sorted(s1)==sorted(s2)):
    print("both are anagrams")
else:
    print("both strings are not anagrams")


