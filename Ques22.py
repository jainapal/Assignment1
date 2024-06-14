# Write a python program that returns the minimum and maximum values
#in a list of numbers.
min=0
max=0
L1=[4,6,1919,577657,76465467.89,0]
for i in L1:
    if(i>max): max=i
    if(i<min): min=i
print("Maximum number: " ,max)
print("Minimun number: " ,min)