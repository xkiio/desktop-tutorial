#list to store ordered pizzas
order_list = ['Margherita','Pepperoni','Hawaiian','Cheese']
#list to store pizzas prices
order_cost = [8.50, 8.50, 8.50, 8.50,]

cost_details = {"name": "Mark","phone": "1234567876","house": "45","street": "harry","suburb": "howick"}



print("\n Customer Name: {} Customer Phone: \n{} Customer House Number: \n{} Customer Street Name: \n{} Customer Suburb : \n{}" .format(cost_details['name'],cost_details['phone'], cost_details['house'],cost_details['street'], cost_details['suburb']))

count = 0
for item in order_list:
    print("Ordered: {} Cost ${:.2f}".format(item, order_cost[count]))
    count = count+1



