# 1. What are Operators?
# - Operators are symbols or keywords used to perform operations on values and variables.

# - Python provides seven main types of operators:
    # 1. Arithmetic Operators
    # 2. Assignment Operators
    # 3. Comparison Operators
    # 4. Logical Operators
    # 5. Bitwise Operators
    # 6. Membership Operators
    # 7. Identity Operators


# 2. Arithmetic Operators
# - Arithmetic operators are used to perform mathematical calculations.

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Exponentiation:", a ** b)


# 3. Assignment Operators
# Assignment operators are used to assign or update the value of a variable.

a = 10

a += 5
print(a)

a -= 3
print(a)

a *= 2
print(a)

a /= 4
print(a)


# 4. Comparison Operators
# - Comparison operators are used to compare two values.
# - The result of a comparison is always True or False.

a = 10
b = 5

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


# 5. Logical Operators
# - Logical operators are used to combine multiple conditions.

# and   Returns True if all conditions are True
# or    Returns True if at least one condition is True
# not   Reverses the result

marks = 85

print(marks >= 40 and marks <= 100)
print(marks < 40 or marks > 90)
print(not marks < 40)


# 6. Bitwise Operators
# - Bitwise operators perform operations on the binary representation of integer values.

a = 10
b = 3

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)


# 7. Membership Operators
# - Membership operators are used to check whether a value exists in a collection.

# in       Checks whether a value exists
# not in   Checks whether a value does not exist

numbers = [10, 20, 30, 40]

print(20 in numbers)
print(50 in numbers)
print(50 not in numbers)


# 8. Identity Operators
# - Identity operators are used to check whether two variables refer to the same object.

# is       Checks whether two variables refer to the same object
# is not   Checks whether two variables refer to different objects

a = [10, 20]
b = a
c = [10, 20]

print(a is b)
print(a is c)
print(a is not c)


# Key Points to Remember:
# 1. Operators are used to perform operations on values and variables.
# 2. Arithmetic operators are used for mathematical calculations.
# 3. Assignment operators are used to assign or update values.
# 4. Comparison operators compare two values and return True or False.
# 5. Logical operators are used to combine conditions.
# 6. Bitwise operators work with the binary representation of integers.
# 7. Membership operators check whether a value exists in a collection.
# 8. Identity operators check whether two variables refer to the same object.
# 9. == compares values.
# 10. is compares object identity.