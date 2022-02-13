import random
from random import randint

#List of random names
names = ["Mark","Pheobe","Sally","Michael","Joyce","Andy", "Hunter","Nuno","Bea","Grace"]

def welcome():
    """
    Purpose: to generate a random name for the list and and print out
    a welcome message.
    Parameters: none
    Returns: none
    """
    num = randint(0,9)
    name = (names[num])
    print("**Welcome to Dream Pizza**")
    print("***My name is",name, "***")
    print("**I'll be here to help you order your Dream pizza**")


def main():
    welcome()
    """
    Purpose: to run all functions.
    Parameters: none
    Returns: none
    """

main()