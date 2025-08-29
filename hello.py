import random

print("hello world")

def start():
    name = input("What's your name")
    age = range(15,31)
    ans = None
    while ans != "Y" or ans != "N":
        ans = input("Is this your age " + str(age) + "? (Y/N)")
    if ans == "N":
        print("rats")
    else:
        print(name + " is " + str(age) + " years old.")
