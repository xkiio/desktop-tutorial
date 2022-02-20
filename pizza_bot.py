#Pizza bot programme
import random
from random import randint

#List of random names
names = ["Mark","Pheobe","Sally","Michael","Joyce","Andy", "Hunter","Nuno","Bea","Grace"]

#Welcome message with random name
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
    print("**I'll be here to help you order your Dream Pizza**")

#Menu for pickup or delivery

def pickup():
    print ("Is your order for pickup or delivery?")
    print ("For pickup, please enter 1 ")
    print ("For delivery, please enter 2 ")

    while True:
        try:
            delivery = int(input("Please enter a number: "))
            if delivery >= 1 and delivery <= 2:
                if delivery == 1:
                    print ("Pickup")
                    break

                elif delivery == 2:
                    print ("Delivery")
                    break
            else:
                print("The number must be 1 or 2. ")
        except ValueError:
            print ("That is not a valid number.")
            print ("Please enter 1 or 2.")

# Pick up information - name and phone number






#Delivery information - name address and phone





#Choose total number of pizzas - max 5






#Pizza menu






#Pizza order - from menu - print each pizza ordered with cast





# Print order out - including if order is del or pick up and names and price of each pizza - total cost including any delivery charge




#Ability to cancel or proceed with order





#Option for new order or exit







#Main function
def main():
    """
    Purpose: to run all functions.
    Parameters: none
    Returns: none
    """
    welcome()
    pickup()

main()