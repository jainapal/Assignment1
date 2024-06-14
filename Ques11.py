 # Write a python program that generates the first n numbers in the
#Fibonacci sequence.
l=[0,1]
def fibonacci(n):
    if(n<0):
        print("Incorrect input")
    else:
        l.append(fibonacci(n-1)+fibonacci(n-2))
        return l[n]
        
N=int(input("enter number till you want to print series"))
fibonacci(N)