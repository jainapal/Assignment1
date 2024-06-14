# Write a program that reads multiple lines of input from the user until they
#enter an empty line, then prints all the lines.

lines=[]
print('Enter line of text(press enter on an empty line to stop:)')
while True:
    line=input()
    if line=="":
        break
    lines.append(line)
print("\n You entered:")
for line in lines:
    print(lines)