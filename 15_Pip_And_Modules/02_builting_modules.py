# 1. The math Module
# - Provides mathematical functions.
# - Useful for numerical calculations.

import math

print(math.sqrt(64))
print(math.ceil(4.3))
print(math.floor(4.8))
# Output:
# 8.0
# 5
# 4


# 2. The statistics Module
# - Provides basic statistical calculations.
# - Useful for learning data analysis.

import statistics

car_prices = [500000, 800000, 1200000, 1500000]

print(statistics.mean(car_prices))
print(statistics.median(car_prices))
# Output:
# 1000000
# 1000000.0


# 3. The random Module
# - Generates pseudo-random values.
# - Useful for simulations and practice datasets.

import random

car_prices = [500000, 800000, 1200000, 1500000]

print(random.choice(car_prices))
# Output:
# One randomly selected price from the list.