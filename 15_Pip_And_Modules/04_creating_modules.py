# 1. Importing Our Own Module
import car_utils


# 2. Creating Car Price Data
car_prices = [500000, 800000, 1200000, 1500000]


# 3. Using Functions from the Module
average_price = car_utils.calculate_average_price(car_prices)

print(average_price)
# Output:
# 1000000.0


# 4. Finding Expensive Cars
expensive_cars = car_utils.get_expensive_cars(car_prices)

print(expensive_cars)
# Output:
# [1200000, 1500000]