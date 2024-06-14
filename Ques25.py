# Write a program that copies the contents of one text file to another.
firstfile=open("firstfile.txt","r")
secondfile=open("secondfile.txt","a")
for i in firstfile:
    secondfile.write(i)