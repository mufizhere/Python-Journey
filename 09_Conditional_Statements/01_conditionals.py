# 1. What are Conditionals?
# - Conditionals are used to make decisions in a Python program.
# - A conditional checks whether a condition is True or False.
# - Python provides if, elif, and else statements for conditional execution.


# 2. If Condition
# - The if statement executes a block of code only when the condition is True.

# Syntax:
# if condition:
#     code

age = 20

if age >= 18:
    print("You are an adult.")  # Output: You are an adult.


# 3. If-Else Condition
# - The if block runs when the condition is True.
# - The else block runs when the condition is False.

# Syntax:
# if condition:
#     code
# else:
#     code

age = 16

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")  # Output: You are a minor.


# 4. If-Elif-Else Condition
# - elif means "else if".
# - It is used when we need to check multiple conditions.
# - Python checks the conditions from top to bottom.
# - The first True condition is executed.

# Syntax:
# if condition:
#     code
# elif condition:
#     code
# else:
#     code

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")  # Output: Grade B
else:
    print("Grade C")