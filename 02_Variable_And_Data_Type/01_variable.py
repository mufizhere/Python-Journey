# 1. What is a Variable?
# - A variable is a name used to store a value.
# - The value of a variable can be changed during program execution.
# - A variable is created by assigning a value using the = operator.
# - Variables can store different types of data.

name = "Mufiz"                  # String
age = 20                        # Integer
height = 5.8                    # Float
is_student = True               # Boolean
skills = ["Python", "SQL"]      # List


# 2. Accessing Variable Values
# - Use the variable name to access its stored value.
first_name = "Mufiz"
last_name = "Parasara"
age = 20

print(first_name)
print(last_name)
print(age)


# 3. Printing Variables with Labels
# - We can add a label to make the output easier to understand.
print("First Name:", first_name)
print("Last Name:", last_name)
print("Age:", age)


# 4. Finding the Length of a String
# - The len() function returns the number of characters in a string.
print("First Name Length:", len(first_name))
print("Last Name Length:", len(last_name))


# 5. Assigning Multiple Variables
# - Python allows multiple variables to be assigned in one statement.
first_name, last_name, country, age, is_student = (
    "Mufiz",
    "Parasara",
    "India",
    20,
    True
)

print(first_name)
print(last_name)
print(country)
print(age)
print(is_student)


# Key Points to Remember:
# 1. A variable is used to store a value.
# 2. The = operator is used to assign a value to a variable.
# 3. A variable can store different types of data.
# 4. Use meaningful variable names.
# 5. Variable values can be changed during program execution.
# 6. Python allows multiple variables to be assigned in one statement.
# 7. Variables are important for storing and processing data in Data Science.