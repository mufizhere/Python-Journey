# 1. What is a Function?
# - A function is a reusable block of code designed to perform a specific task.
# - Functions help us avoid writing the same code multiple times.
# - We create a custom function using the def keyword.
# - A function runs only when we call it.


# 2. Creating a Function
def greet():
    print("Hello, welcome to Python!")


# 3. Calling a Function
# - We call a function by writing its name followed by parentheses.
# - Calling a function means executing the function.
greet()                 

# Output:
# Hello, welcome to Python!


# 4. Function Without Parameters
# - A function can work without receiving any outside information.
# - The values can be created inside the function.

def add_numbers():
    num1 = 10
    num2 = 20
    total = num1 + num2
    print(total)


add_numbers()
# Output:
# 30


# 5. Why Do We Use Functions?
# - Functions make code reusable.
# - Functions make code easier to understand.
# - Functions reduce repeated code.
# - Functions make large programs easier to organize.

def student_info():
    print("Name: Mufiz")
    print("Course: Data Science")


student_info()
# Output:
# Name: Mufiz
# Course: Data Science

student_info()
# Output:
# Name: Mufiz
# Course: Data Science