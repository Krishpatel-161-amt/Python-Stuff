toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

# Count 42 slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# number of pizzas
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " diffrent kinds of pizza!")

# new 2d list with [price, topping_name]
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

# sort the price by ascending order
pizza_and_prices.sort()
print(pizza_and_prices)

# store the 1st element 
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

# store the last element
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

# remove() 
pizza_and_prices.remove([7, "anchovies"])
print(pizza_and_prices)

# insert()
pizza_and_prices.insert(4,[2.5, "pepperoni"])
print(pizza_and_prices)

# slicing
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
