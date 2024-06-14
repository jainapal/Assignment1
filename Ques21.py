# Write a python program that counts the occurrences of a specific element
#in a list.
n=int(input("Enter no. of elements: "))
list1=[]
for i in range(n):
    element=input()
    list1.append(element)
print("list1:",list1)
find=input("element need to find: ")
cnt=0
for j in list1:
    if j==find:
        cnt=cnt+1
print(cnt)
        
