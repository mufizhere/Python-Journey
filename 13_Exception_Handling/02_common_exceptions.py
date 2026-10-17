# 1. Common Python Exceptions
# - Python provides different types of exceptions.
# - The most common exceptions are:
    # ValueError
    # TypeError
    # ZeroDivisionError
    # FileNotFoundError
    # IndexError
    # KeyError


# 2. ValueError
# - ValueError occurs when a value has an invalid format.
try:
    number = int("abc")

except ValueError:
    print("Invalid value")

# Output: Invalid value


# 3. TypeError
# - TypeError occurs when incompatible data types are used together.
try:
    result = 10 + "5"

except TypeError:
    print("Invalid data types")

# Output: Invalid data types


# 4. ZeroDivisionError
# - ZeroDivisionError occurs when a number is divided by zero.
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

# Output: Cannot divide by zero


# 5. IndexError
# - IndexError occurs when we access an index that does not exist.
numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Index does not exist")


# 6. KeyError
# - KeyError occurs when we access a dictionary key that does not exist.
student = {
    "name": "Mufiz",
    "course": "Data Science"
}

try:
    print(student["age"])

except KeyError:
    print("Key does not exist")


# 7. FileNotFoundError
# - FileNotFoundError occurs when the requested file does not exist.
try:
    file = open("data.txt")

except FileNotFoundError:
    print("File not found")