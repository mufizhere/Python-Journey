# car_utils.py

# 1. Creating a Reusable Function
def calculate_average_price(prices):
    return sum(prices) / len(prices)


# 2. Creating Another Function
def get_expensive_cars(prices):
    return [price for price in prices if price >= 1000000]