# 1. What is a Tuple?
# - A tuple is a collection of multiple items stored in a single variable.
# - Tuples are ordered and immutable.
# - Immutable means we cannot change, add, or remove items after creation.

fruits = ("banana", "orange", "mango", "lemon")
print(fruits)           # Output: ('banana', 'orange', 'mango', 'lemon')


# 2. Creating an Empty Tuple
empty_tuple = ()
print(empty_tuple)      # Output: ()

# - We can also create an empty tuple using tuple()
empty_tuple = tuple()
print(empty_tuple)      # Output: ()

# - Creating a Tuple With Items
fruits = ("banana", "orange", "mango", "lemon")
print(fruits)           # Output: ('banana', 'orange', 'mango', 'lemon')

# - Finding the Length of a Tuple
fruits = ("banana", "orange", "mango", "lemon")
print(len(fruits))      # Output: 4

# - Tuple Can Contain Different Data Types
student = ("Mufiz", 20, "Data Science", True)
print(student)          # Output: ('Mufiz', 20, 'Data Science', True)

# - Checking Whether an Item Exists
fruits = ("banana", "orange", "mango", "lemon")
print("orange" in fruits)   # Output: True
print("apple" in fruits)    # Output: False


# - 3. Tuples Are Immutable
fruits = ("banana", "orange", "mango", "lemon")

# fruits[0] = "apple"
# This gives:
# TypeError: 'tuple' object does not support item assignment