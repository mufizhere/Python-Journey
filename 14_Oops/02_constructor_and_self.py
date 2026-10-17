# 1. What is a Constructor?
# - A constructor initializes an object when it is created.
# - In Python, __init__() is used to initialize object attributes.


# 2. What is self?
# - self refers to the current object.
# - It allows an object to access its own attributes and methods.


# 3. Creating a Car Class with a Constructor
# - __init__() runs automatically when an object is created.
# - brand, model, and color are parameters.
# - self.brand stores the brand in the current object.
# - self.model stores the model in the current object.
# - self.color stores the color in the current object.

class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color


# 4. Creating Objects
# - Each object receives different values.
# - car1 represents a black Toyota Fortuner.
# - car2 represents a blue BMW M5.

car1 = Car("Toyota", "Fortuner", "Black")
car2 = Car("BMW", "M4", "Blue")


# 5. Accessing Object Attributes

print(car1.brand)
print(car1.model)
print(car1.color)

print(car2.brand)
print(car2.model)
print(car2.color)

# Output:
# Toyota
# Fortuner
# Black
# 
# BMW
# M5
# Blue