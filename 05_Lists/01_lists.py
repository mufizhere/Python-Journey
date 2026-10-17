# 1. What is a List?
# - A list is a collection of multiple items stored in a single variable.
# - Lists are ordered, changeable, and allow duplicate values.

fruits = ["banana", "orange", "mango", "lemon"]
print(fruits)           # Output: ['banana', 'orange', 'mango', 'lemon']


# 2. Creating an Empty List
empty_list = []
print(empty_list)       # Output: []
print(len(empty_list))  # Output: 0

# - A List Can Contain Different Data Types:
student = ["Mufiz", 20, "Data Science", True]
print(student)          # Output: ['Mufiz', 20, 'Data Science', True]

# - Finding the Length of a List:
fruits = ["banana", "orange", "mango", "lemon"]
print(len(fruits))      # Output: 4

# - Checking Whether an Item Exists:
fruits = ["banana", "orange", "mango", "lemon"]
print("banana" in fruits)   # Output: True
print("apple" in fruits)    # Output: False


# - 3. Modifying Items in a List
fruits = ["banana", "orange", "mango", "lemon"]

fruits[0] = "apple"
print(fruits)           # Output: ['apple', 'orange', 'mango', 'lemon']

fruits[1] = "grapes"
print(fruits)           # Output: ['apple', 'grapes', 'mango', 'lemon']