# 1. What is the else Block?
# - The else block runs only when no exception occurs.

# Syntax:
# try:
#     code
#
# except:
#     error handling
#
# else:
#     code when no error occurs


# 2. Example of else
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("You entered:", number)


# 3. What is the finally Block?
# - The finally block always runs.
# - It runs whether an exception occurs or not.
# - It is commonly used for cleanup operations.


# 4. Example of finally
try:
    number = 10 / 2

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Program execution completed.")

# Output:
# 5.0
# Program execution completed.


# 5. Using try, except, else and finally
try:
    number = int(input("Enter a number: "))

    result = 100 / number

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Program execution completed.")


# 6. Important Difference
# - try contains code that may cause an error.
# - except handles the error.
# - else runs when there is no error.
# - finally always runs.