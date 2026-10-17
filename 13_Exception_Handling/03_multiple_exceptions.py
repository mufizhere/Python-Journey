# 1. What are Multiple Exceptions?
# - A program can have different types of exceptions.
# - We can use multiple except blocks to handle them separately.


# 2. Multiple except Blocks
try:
    number = int(input("Enter a number: "))

    result = 100 / number

    print("Result:", result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# 3. Example with User Information
try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print(f"Name: {name}")
    print(f"Age: {age}")

except ValueError:
    print("Age must be a number.")

except TypeError:
    print("Invalid data type.")


# 4. Handling Any Exception
# - Exception can be used when we want to handle unexpected errors.
try:
    number = int(input("Enter a number: "))
    result = 100 / number

    print(result)

except Exception as e:
    print("Error:", e)


# 5. Best Practice
# - Handle specific exceptions when possible.
# - Use Exception as e when you need general error handling.
# - Avoid using an empty except block in professional programs.