# 1. What are Attributes?
# - Attributes are variables associated with an object or class.
# - Instance attributes store information specific to each object.
# - Examples: brand, model, color, and speed.


# 2. What are Methods?
# - Methods are functions defined inside a class.
# - Instance methods usually take self as their first parameter.
# - They define the actions an object can perform.


# 3. Creating a Car Class

class Car:

    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Speed: {self.speed} km/h")

    def accelerate(self, amount):
        self.speed += amount
        print(f"Speed increased to {self.speed} km/h")

# - brand, model, and speed are instance attributes.
# - display_info() is an instance method.
# - accelerate() is another instance method.
# - accelerate() increases the current object's speed.


# 4. Creating an Object
car1 = Car("Toyota", "Fortuner", 60)


# 5. Calling Methods
car1.display_info()
print()
car1.accelerate(20)

# Output:
# Brand: Toyota
# Model: Fortuner
# Speed: 60 km/h
#
# Speed increased to 80 km/h