import random

print("hello world")

def start():
    name = input("What's your name")
    age = random.randrange(15,30)
    ans = None
    while ans != "Y" or ans != "N":
        ans = input("Is this your age " + str(age) + "? (Y/N)")
    if ans == "N":
        print("rats")
    else:
        print(name + " is " + str(age) + " years old.")

start()
