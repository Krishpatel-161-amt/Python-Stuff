# sets available hairstyles
hairstyles = [
    "bouffant", "pixie", "dreadlocks", "crew",
    "bowl", "bob", "mohawk", "flattop"
]
# sets haircut prices
prices = [30, 25, 40, 20, 20, 35, 50, 35]
# sets haircuts sold last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# starts total price at 0
total_price = 0

# prints header for prices
print("=== Listing the prices and sum of prices ===")
# loops through prices
for price in prices:
    # prints each price
    print(price)
    # adds to total
    total_price += price

# prints header for average
print("=== Average price ===")
# calculates average price
average_price = total_price / len(prices)
# prints average price
print("Average Haircut Price:", average_price)

# prints header for new prices
print("=== New prices ===")
# creates list with 5 dollar discount
new_prices = [price - 5 for price in prices]
# prints new prices
print(new_prices)

# starts total revenue at 0
total_revenue = 0

# prints header for revenue
print("=== Total revenue ===")
# loops through each style
for i in range(len(hairstyles)):
    # adds to total revenue
    total_revenue += prices[i] * last_week[i]
# prints total revenue
print("Total Revenue:", total_revenue)

# prints header for daily revenue
print("=== Average daily revenue ===")
# calculates daily average
average_daily_revenue = total_revenue / 7
# prints daily average
print(average_daily_revenue)

# prints header for cheap cuts
print("Hairstyles under $30")
# finds styles under 30 dollars
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
# prints cheap styles
print(cuts_under_30)
