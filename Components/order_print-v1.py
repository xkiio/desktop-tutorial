#lists of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]
#list to store ordered pizzas
order_list = ['Margherita','Pepperoni','Hawaiian','Cheese']
#list to store pizzas prices
order_cost = [8.50, 8.50, 8.50, 8.50,]

count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count+1



