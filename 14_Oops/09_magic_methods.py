# 1. What are Magic Methods?
# - Magic methods are special methods surrounded by double underscores.
# - They allow objects to work with Python's built-in operations.


# 2. The __init__() Method
# - Initializes an object when it is created.

# 3. The __str__() Method
# - Returns a readable string representation of an object.

# 4. The __repr__() Method
# - Returns a representation useful for debugging.

# 5. The __len__() Method
# - Defines the result of calling len() on an object.


class Car:

    def __init__(self, brand, model, features):
        self.brand = brand
        self.model = model
        self.features = features

    def __str__(self):
        return f"{self.brand} {self.model}"

    def __repr__(self):
        return (
            f"Car(brand={self.brand!r}, "
            f"model={self.model!r}, "
            f"features={self.features!r})"
        )

    def __len__(self):
        return len(self.features)


# 6. Creating an Object
car = Car(
    "Toyota",
    "Fortuner",
    ["Air Conditioning", "ABS", "Cruise Control"]
)


# 7. Displaying the Object
print(car)

# Output:
# Toyota Fortuner


# 8. Displaying the Debug Representation
print(repr(car))

# Output:
# Car(brand='Toyota', model='Fortuner',
#     features=['Air Conditioning', 'ABS', 'Cruise Control'])


# 9. Counting the Features
print(len(car))

# Output:
# 3