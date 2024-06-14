# Write a program that reads data from a CSV file and prints it to the
#console.
with open("/Users/jainapal/Downloads/temperatures.csv", 'r') as file:
            content = file.read()
            print(content)