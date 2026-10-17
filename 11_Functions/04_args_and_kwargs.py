# 1. What is *args
# - *args allows a function to accept any number of positional arguments.
# - Inside the function, args is treated as a tuple.

# Syntax:
# def function_name(*args):
#     code

def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

print(add_numbers(10, 20))
# Output:
# 30

print(add_numbers(10, 20, 30, 40))
# Output:
# 100


# 2. What is **kwargs 
# - **kwargs allows a function to accept any number of keyword arguments.
# - Inside the function, kwargs is treated as a dictionary.

# Syntax:
# def function_name(**kwargs):
#     code

def student_info(**details):
    print(details)


student_info(name="Mufiz", course="Data Science", age=20)
# Output:
# {'name': 'Mufiz', 'course': 'Data Science', 'age': 20}



# 3. *args vs **kwargs

# *args
# - Accepts multiple positional arguments.
# - Stored as a tuple.

def numbers(*args):
    print(args)

numbers(10, 20, 30)
# Output:
# (10, 20, 30)


# **kwargs
# - Accepts multiple keyword arguments.
# - Stored as a dictionary.

def details(**kwargs):
    print(kwargs)

details(name="Mufiz", course="Data Science")
# Output:
# {'name': 'Mufiz', 'course': 'Data Science'}