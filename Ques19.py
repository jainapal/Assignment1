# Write a python program that removes all punctuation from a given string.
from string import punctuation


def remove_punctuation(str):
    ans=" "
    punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in str:
        if char not in punctuation:
            ans+=char
    return ans

a=input("Enter your string:")
print(remove_punctuation(a))





