# 1. What is raise?
# - The raise keyword is used to manually create an exception.
# - It is useful when we want to stop a program when a specific condition is not valid.


# 2. Basic Example
age = 15

if age < 18:
    raise ValueError("Age must be 18 or above.")


# 3. Using raise with try and except
try:

    age = int(input("Enter your age: "))

    if age < 18:
        raise ValueError("Age must be 18 or above.")

    print("Access allowed.")

except ValueError as e:
    print("Error:", e)


# 4. Example with Data Validation
def calculate_average(marks):

    if len(marks) == 0:
        raise ValueError("Marks list cannot be empty.")

    return sum(marks) / len(marks)


try:
    marks = [80, 75, 90]
    average = calculate_average(marks)

    print("Average:", average)

except ValueError as e:
    print("Error:", e)


# 5. Why Do We Use raise?
# - raise is useful for data validation.
# - It helps us stop invalid data.
# - It allows us to create meaningful error messages.
# - It is commonly used in functions and applications.