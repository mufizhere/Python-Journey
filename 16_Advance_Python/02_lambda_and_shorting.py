# LAMBDA FUNCTIONS AND SORTING


# 1. What Is a Lambda Function?
# - A small anonymous function.
# - Written using the lambda keyword.
# - Contains a single expression.

square = lambda number: number ** 2

print("Square:", square(5))
# Output:
# Square: 25


# 2. Lambda with Multiple Arguments

calculate_discount = lambda price, discount: (
    price * (1 - discount / 100)
)

print("Discounted Price:", calculate_discount(1000000, 10))
# Output:
# Discounted Price: 900000.0


# 3. The sorted() Function
# - Returns a new sorted list.
# - The original list remains unchanged.

car_prices = [1200000, 500000, 1500000, 800000]

sorted_prices = sorted(car_prices)

print("Original Prices:", car_prices)
print("Sorted Prices:", sorted_prices)
# Output:
# Original Prices: [1200000, 500000, 1500000, 800000]
# Sorted Prices: [500000, 800000, 1200000, 1500000]


# 4. Sorting in Descending Order
# reverse=True sorts from largest to smallest.

sorted_prices_descending = sorted(
    car_prices,
    reverse=True
)

print("Descending Prices:", sorted_prices_descending)
# Output:
# Descending Prices: [1500000, 1200000, 800000, 500000]


# 5. Sorting Car Records Using Lambda
# Each car is represented by a dictionary.

cars = [
    {"brand": "Toyota", "price": 1200000},
    {"brand": "Honda", "price": 900000},
    {"brand": "BMW", "price": 7500000},
    {"brand": "Hyundai", "price": 800000}
]

cars_sorted_by_price = sorted(
    cars,
    key=lambda car: car["price"]
)

print("\nCars Sorted by Price:")

for car in cars_sorted_by_price:
    print(car["brand"], car["price"])
# Output:
# Cars Sorted by Price:
# Hyundai 800000
# Honda 900000
# Toyota 1200000
# BMW 7500000


# 6. Finding the Cheapest and Most Expensive Cars

cheapest_car = min(cars, key=lambda car: car["price"])
most_expensive_car = max(cars, key=lambda car: car["price"])

print("\nCheapest Car:", cheapest_car["brand"])
print("Most Expensive Car:", most_expensive_car["brand"])
# Output:
# Cheapest Car: Hyundai
# Most Expensive Car: BMW