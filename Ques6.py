# Write a program that reads the content of a text file and prints it to the
#console.
with open("/Users/jainapal/Downloads/temperatures.csv", 'r') as file:
            content = file.read()
            print(content)