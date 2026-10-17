# 1. What is an Exception?
# - An exception is an error that occurs while a Python program is running.
# - An exception can stop the normal execution of a program.
# - Exception handling allows us to handle errors without crashing the program.


# 2. Why Do We Need Exception Handling?
# - It prevents the program from stopping unexpectedly.
# - It allows us to display meaningful error messages.
# - It makes programs more reliable.
# - It is useful when working with user input, files and data.


# 3. try and except
# - The try block contains code that may cause an exception.
# - The except block handles the exception.

# Syntax:
# try:
#     code that may cause an error
#
# except:
#     code that handles the error


# 4. Basic Example
try:
    number = 10 / 0

except:
    print("Something went wrong")

# Output: Something went wrong


# 5. Handling User Input
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except:
    print("Invalid input")


# 6. Exception as e
# - We can store the exception in a variable using as.
try:
    number = 10 / 0

except Exception as e:
    print("Error:", e)

# Output: Error: division by zero