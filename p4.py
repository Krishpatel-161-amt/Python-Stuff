hairstyles = [
    "bouffant",
    "pixie",
    "dreadlocks",
    "crew",
    "bowl",
    "bob",
    "mohawk",
    "flattop",
]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

# This calculates the sum of prices
print("=== Listing the prices and sum of prices ===")
for price in prices:
    print(price)
    total_price += price

# This returns the no. of prices
print("=== Average price ===")
average_price = total_price / 8
print("Average Haircut Price:", average_price)

# List comprehension to minus 5 from prices
print("=== New prices ===")
new_prices = [price - 5 for price in prices]
print(new_prices)

total_revenue = 0

# Total revenue
print("=== Total revenue ===")
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print("Total Revenue:", total_revenue)

# Daily revenue
print("=== average daily revenue ===")
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# Cuts under $30
print("Hairstyles under $30")
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
