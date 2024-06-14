# Write a program in python that counts the frequency of each character in
#a string.
str=input("enter string: ")
find=input("char need to find :")
cnt=0
for i in str:
    if(i==find):
        cnt+=1
print("frequency of {} is".format(find),cnt)