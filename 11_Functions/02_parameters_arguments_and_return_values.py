# 1. What is a Parameter?
# - A parameter is a variable written inside the function definition.
# - It allows a function to receive data.

def greet(name):
    print("Hello", name)


# 2. What is an Argument?
# - An argument is the actual value passed to a function.
# - "Mufiz" is the argument in this example.

greet("Mufiz")
# Output:
# Hello Mufiz


# 3. Function with Two Parameters
# - A function can have more than one parameter.

def add_numbers(num1, num2):
    total = num1 + num2
    print(total)

add_numbers(10, 20)
# Output:
# 30


# 4. What is Return?
# - return sends a value back from the function.
# - The returned value can be stored in a variable or used in another calculation.
# - return also stops the function at that point.

def add_numbers(num1, num2):
    total = num1 + num2
    return total

result = add_numbers(10, 20)
print(result)
# Output:
# 30


# 5. Return vs Print
# - print() displays a value on the screen.
# - return sends a value back to the place where the function was called.

def calculate_square(number):
    return number * number

result = calculate_square(5)
print(result)
# Output:
# 25


# 6. Using the Returned Value
# - A returned value can be used in another calculation.

def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(10, 20)
final_result = result * 2
print(final_result)
# Output:
# 60