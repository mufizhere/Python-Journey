# 1. What is a Default Parameter?
# - A default parameter has a value already assigned in the function definition.
# - If we do not provide a value when calling the function, Python uses the default value.

# Syntax:
# def function_name(parameter=value):
def greet(name="Mufiz"):
    print("Hello", name)

greet()
# Output:
# Hello Mufiz


# 2. Changing the Default Value
# - We can provide our own value when calling the function.
# - The provided value replaces the default value.

def greet(name="Mufiz"):
    print("Hello", name)

greet("Zoro")
# Output:
# Hello Zoro


# 3. Default Parameter with Multiple Parameters

def student_info(name="Mufiz", course="Data Science"):
    print("Name:", name)
    print("Course:", course)

student_info()
# Output:
# Name: Mufiz
# Course: Data Science

student_info("Zoro", "Python")
# Output:
# Name: Zoro
# Course: Python


# 4. What are Keyword Arguments?
# - Keyword arguments are arguments passed using the parameter name.
# - The parameter name and value are written together.

def student_info(name, course):
    print("Name:", name)
    print("Course:", course)

student_info(name="Mufiz", course="Data Science")
# Output:
# Name: Mufiz
# Course: Data Science


# 5. Keyword Arguments and Order
# - When using keyword arguments, the order does not matter.
# - Python matches each value with its parameter name.

def student_info(name, course):
    print("Name:", name)
    print("Course:", course)

student_info(course="Data Science", name="Mufiz")
# Output:
# Name: Mufiz
# Course: Data Science


# 6. Positional Arguments vs Keyword Arguments

# Positional argument:
# - Values are matched according to their position.
student_info("Mufiz", "Data Science")

# Keyword argument:
# - Values are matched according to their parameter name.
student_info(name="Mufiz", course="Data Science")