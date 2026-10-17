# 1. What are Class Attributes?
# - Class attributes belong to the class.
# - They can be shared by all instances.
# - Example: The number of wheels on a standard four-wheel car.

class Car:

    wheels = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car1 = Car("Toyota", "Fortuner")
car2 = Car("BMW", "M5")

print(car1.wheels)
print(car2.wheels)
# Output:
# 4
# 4


# 2. What are Class Methods?
# - A class method receives the class as its first argument.
# - The first parameter is conventionally named cls.
# - @classmethod defines a class method.

class Car:

    vehicle_type = "Four-Wheeler"

    @classmethod
    def display_vehicle_type(cls):
        print(cls.vehicle_type)


Car.display_vehicle_type()
# Output:
# Four-Wheeler


# 3. What are Static Methods?
# - Static methods do not automatically receive self or cls.
# - They are useful for utility operations related to a class.
# - @staticmethod defines a static method.

class Car:

    @staticmethod
    def is_valid_speed(speed):
        return speed >= 0


print(Car.is_valid_speed(80))
print(Car.is_valid_speed(-10))
# Output:
# True
# False