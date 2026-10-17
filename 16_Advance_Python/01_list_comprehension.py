# LIST COMPREHENSION


# 1. What Is List Comprehension?
# - A concise way to create a new list.
# - It can transform or filter existing data.
# - Useful for simple data-processing operations.


# 2. Basic List Comprehension
# Syntax: [expression for item in iterable]

car_prices = [500000, 800000, 1200000, 1500000]
prices_in_lakhs = [price / 100000 for price in car_prices]

print("Prices in Lakhs:", prices_in_lakhs)
# Output:
# Prices in Lakhs: [5.0, 8.0, 12.0, 15.0]


# 3. List Comprehension with a Condition
# Syntax: [expression for item in iterable if condition]
# Only values satisfying the condition are included.

car_prices = [500000, 800000, 1200000, 1500000]

expensive_cars = [
    price for price in car_prices
    if price >= 1000000
]

print("Expensive Cars:", expensive_cars)
# Output:
# Expensive Cars: [1200000, 1500000]


# 4. Transforming Text Data
# strip() removes surrounding whitespace.
# title() capitalizes the beginning of each word.

car_brands = [" toyota ", "HONDA", " bmw ", "ford"]

cleaned_brands = [
    brand.strip().title()
    for brand in car_brands
]

print("Cleaned Brands:", cleaned_brands)
# Output:
# Cleaned Brands: ['Toyota', 'Honda', 'Bmw', 'Ford']


# 5. Conditional Expression
# Syntax: value_if_true if condition else value_if_false
# This transforms every item based on a condition.

car_prices = [500000, 800000, 1200000, 1500000]

price_categories = [
    "Expensive" if price >= 1000000 else "Affordable"
    for price in car_prices
]

print("Price Categories:", price_categories)
# Output:
# Price Categories: ['Affordable', 'Affordable', 'Expensive', 'Expensive']


# 6. Data Science Example: Convert Prices to USD
# Demonstrates applying a transformation to each value.
# The exchange rate below is illustrative, not a live rate.

car_prices_inr = [500000, 1000000, 1500000]

inr_to_usd_rate = 85

car_prices_usd = [
    round(price / inr_to_usd_rate, 2)
    for price in car_prices_inr
]

print("Prices in USD:", car_prices_usd)
# Output:
# Prices in USD: [5882.35, 11764.71, 17647.06]