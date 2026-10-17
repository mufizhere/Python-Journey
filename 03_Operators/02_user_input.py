# 1. What is User Input?
# - User input is the process of taking data from the user while a Python program is running.
# - Python provides the input() function to take user input.


# 2. Using the input() Function
# - The input() function displays a message and waits for the user to enter a value.

name = input("Enter your name: ")
print(name)


# 3. Important Point About input()
# - The input() function always returns the user's input as a string.
# - Even when the user enters a number, input() returns it as a string.

name = input("Enter your name: ")

print(name)
print(type(name))


# 4. Converting User Input
# - If we need a number for calculations, we must convert the input to the required data type.

# String to Integer:
age = int(input("Enter your age: "))
print(age)
print(type(age))

# String to Float:
percentage = float(input("Enter your percentage: "))
print(percentage)
print(type(percentage))


# 5. Taking Multiple Types of User Input

name = input("Enter your name: ")
age = int(input("Enter your age: "))
percentage = float(input("Enter your percentage: "))

print("Name:", name)
print("Age:", age)
print("Percentage:", percentage)



# Key Points to Remember:
    # 1. The input() function is used to take user input.
    # 2. input() always returns the entered value as a string.
    # 3. Use int() when an integer is required.
    # 4. Use float() when a decimal number is required.
    # 5. Type conversion is important when performing calculations.
    # 6. User input allows programs to work with dynamic data.
    # 7. User input is commonly used in interactive programs and data collection.