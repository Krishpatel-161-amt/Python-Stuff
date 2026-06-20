# sets pizza toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
# sets pizza prices
prices = [2, 6, 1, 3, 2, 7, 2]

# counts two dollar slices
num_two_dollar_slices = prices.count(2)
# prints count
print(num_two_dollar_slices)

# counts total pizzas
num_pizzas = len(toppings)
# prints total pizzas
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# creates 2d list of pizzas
pizza_and_prices = [
    [2, "pepperoni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"]
]
# prints 2d list
print(pizza_and_prices)

# sorts list by price
pizza_and_prices.sort()
# prints sorted list
print(pizza_and_prices)

# gets cheapest pizza
cheapest_pizza = pizza_and_prices[0]
# prints cheapest
print(cheapest_pizza)

# gets priciest pizza
priciest_pizza = pizza_and_prices[-1]
# prints priciest
print(priciest_pizza)

# removes anchovies
pizza_and_prices.remove([7, "anchovies"])
# prints updated list
print(pizza_and_prices)

# inserts new pepperoni
pizza_and_prices.insert(4, [2.5, "pepperoni"])
# prints updated list
print(pizza_and_prices)

# gets three cheapest pizzas
three_cheapest = pizza_and_prices[:3]
# prints three cheapest
print(three_cheapest)
