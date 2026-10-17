# 1. What is OOP?
# - OOP stands for Object-Oriented Programming.
# - It is a programming approach based on classes and objects.
# - It helps us organize code and reuse functionality.
# - We can use OOP to represent real-world things, such as cars.


# 2. What is a Class?
# - A class is a blueprint for creating objects.
# - It defines the attributes and methods that objects can have.
# - Example: Car is a class.


# 3. Creating a Class

class Car:
    pass


# 4. What is an Object?
# - An object is an instance of a class.
# - We create an object by calling the class name with parentheses.
# - car1 and car2 are two separate objects.
# - Both objects belong to the Car class.

car1 = Car()
car2 = Car()


# 5. Checking the Object Type
print(type(car1))
print(type(car2))

# Output:
# <class '__main__.Car'>
# <class '__main__.Car'>