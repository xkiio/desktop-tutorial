#list of pizza names
pizza_names = ['Margherita','Pepperoni','Hawaiian','Cheese','Italian','Veggie','Vegan','Chicken Deluxe',
                'Mega Meat Lovers','Seafood Deluxe','Apricot Chicken Deluxe','BBQ Chicken Deluxe']
#lists of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

#list to store ordered pizzas
order_list = []
#list to store pizzas prices
order_cost = []

#list to store order cost

def menu():
    number_pizza = 12

    for count in range(number_pizza) :
        print("{} {} ${:.2f}" .format(count+1, pizza_names[count],pizza_prices[count]))

menu()

# ask for total number of pizzas for order
num_pizzas = 0


while True:
    try:
        num_pizzas = int(input("How many pizzas do you want to order? "))
        if num_pizzas >= 1 and num_pizzas <= 5:
            break
        else:
            print("Your order must be between 1 and 5")
    except ValueError:
        print ("That is not a valid number.")
        print ("Please enter 1 or 5")



#Choose pizza from menu
for item in range(num_pizzas):
    while num_pizzas > 0:
        while True:
            try:
                pizza_ordered = int(input("Please choose your pizzas by entering the number from the menu: "))
                if pizza_ordered >= 1 and pizza_ordered <= 12:
                    break
                else:
                    print("Your pizza order must be between 1 and 12.")
            except ValueError:
                print ("That is not a valid number.")
                print ("Please enter a number between 1 and 12.")
        pizza_ordered = pizza_ordered -1
        order_list.append(pizza_names[pizza_ordered])
        order_cost.append(pizza_prices[pizza_ordered])
        print("{} ${:.2f}" .format(pizza_names[pizza_ordered],pizza_prices[pizza_ordered]))
        num_pizzas = num_pizzas-1