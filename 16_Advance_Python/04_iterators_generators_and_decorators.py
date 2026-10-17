# ITERATORS, GENERATORS, AND DECORATORS



# 1. ITERATORS
# - An iterator produces values one at a time.
# - iter() creates an iterator from an iterable.
# - next() retrieves the next available value.

car_brands = ["Toyota", "Honda", "BMW"]
brand_iterator = iter(car_brands)

print(next(brand_iterator))
print(next(brand_iterator))
print(next(brand_iterator))
# Output:
# Toyota
# Honda
# BMW


# 2. GENERATORS
# - A generator function uses yield to produce values one at a time.
# - This can reduce memory usage when processing large sequences.

def generate_car_ids(count):

    for car_id in range(1, count + 1):
        yield car_id


car_ids = generate_car_ids(3)

for car_id in car_ids:
    print("Car ID:", car_id)
# Output:
# Car ID: 1
# Car ID: 2
# Car ID: 3


# 3. GENERATOR FOR PROCESSING CAR PRICES
# - Generate only prices above a threshold.
# - Values are produced as the generator is iterated.

def generate_expensive_prices(prices, threshold):

    for price in prices:

        if price >= threshold:
            yield price


car_prices = [500000, 800000, 1200000, 1500000]

for price in generate_expensive_prices(car_prices, 1000000):
    print("Expensive Price:", price)

# Output:
# Expensive Price: 1200000
# Expensive Price: 1500000


# 4. DECORATORS
# - A decorator adds reusable behavior to a function.
# - Here, the decorator measures execution time.

import time
from functools import wraps

def measure_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        execution_time = end_time - start_time

        print(f"Execution Time: {execution_time:.6f} seconds")

        return result

    return wrapper



# 5. USING THE DECORATOR

@measure_time
def calculate_total_price(prices):

    return sum(prices)


car_prices = [500000, 800000, 1200000, 1500000]
total_price = calculate_total_price(car_prices)

print("Total Price:", total_price)
# Example Output:
# Execution Time: 0.000002 seconds
# Total Price: 4000000

# The execution time varies each time you run the program.