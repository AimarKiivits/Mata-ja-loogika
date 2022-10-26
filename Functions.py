import math


def print_hello():
    print("Hello")

#print_hello()

def get_hello():
    return "Hello"

#print(get_hello())

def ask_name_and_greet_user():
    name = str(input("Name:"))

    if name.capitalize() == "Thanos":
        print("Get out of here, Thanos! Nobody wants to play with you!")

    else:
        print("Hi, " + name.capitalize() + " Would you like to have a Hamburger?")

#ask_name_and_greet_user()

def calculate_hypothenuse_lenght(cathetus_1, cathetus_2):
    hypothenuse = math.sqrt(cathetus_1 ** 2 + cathetus_2 ** 2)
    return hypothenuse


print(calculate_hypothenuse_lenght(3,4))

def calculate_cathetus_lenght(hypothenuse, other_cathetus):
    cathetus = math.sqrt(hypothenuse ** 2 - other_cathetus ** 2)
    return cathetus

print(calculate_cathetus_lenght(5,4))
