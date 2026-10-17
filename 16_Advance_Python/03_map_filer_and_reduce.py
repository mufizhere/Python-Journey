# MAP, FILTER, AND REDUCE


# 1. What Is map()?
# - Applies a function to every item in an iterable.
# - Returns an iterator.
# - Use list() to collect the results into a list.

car_prices = [500000, 800000, 1200000, 1500000]
prices_in_lakhs = list(map(lambda price: price / 100000, car_prices))

print("Prices in Lakhs:", prices_in_lakhs)
# Output:
# Prices in Lakhs: [5.0, 8.0, 12.0, 15.0]


# 2. What Is filter()?
# - Selects items for which a function returns True.
# - Returns an iterator.

car_prices = [500000, 800000, 1200000, 1500000]

expensive_cars = list(filter(lambda price: price >= 1000000, car_prices))

print("Expensive Cars:", expensive_cars)
# Output:
# Expensive Cars: [1200000, 1500000]


# 3. What Is reduce()?
# - Combines items into a single result.
# - Available from the functools module.

from functools import reduce

car_prices = [500000, 800000, 1200000, 1500000]

total_price = reduce(
    lambda total, price: total + price,
    car_prices,
    0
)

print("Total Price:", total_price)
# Output:
# Total Price: 4000000


# 4. Combining map() and filter()
# - First filter expensive cars.
# - Then convert their prices into lakhs.

car_prices = [500000, 800000, 1200000, 1500000]

expensive_prices_in_lakhs = list(
    map(
        lambda price: price / 100000,
        filter(lambda price: price >= 1000000, car_prices)
    )
)

print("Expensive Prices in Lakhs:", expensive_prices_in_lakhs)
# Output:
# Expensive Prices in Lakhs: [12.0, 15.0]


# 5. Calculating an Average Price

car_prices = [500000, 800000, 1200000, 1500000]
average_price = sum(car_prices) / len(car_prices)

print("Average Price:", average_price)
# Output:
# Average Price: 1000000.0