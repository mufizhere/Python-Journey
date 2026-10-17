# 1. What is a Set?
# - A set is a collection of unique items stored in a single variable.
# - Sets are unordered and do not use indexes.
# - Sets do not allow duplicate values.
# - Sets are written using curly brackets {}.

fruits = {"banana", "orange", "mango", "lemon"}
print(fruits)               # Output: {'banana', 'orange', 'mango', 'lemon'}


# 2. Creating an Empty Set
# - To create an empty set, we use set().
empty_set = set()
print(empty_set)            # Output: set()

# - Empty curly brackets {} create a dictionary, not a set.
empty = {}
print(type(empty))          # Output: <class 'dict'>


# 3. Creating a Set with Different Data Types
student = {"Mufiz", 20, "Data Science", True}
print(student)              # Output: {'Mufiz', 20, 'Data Science', True}


# 4. Finding the Length of a Set
# - The len() function returns the number of items in a set.
fruits = {"banana", "orange", "mango", "lemon"}
print(len(fruits))          # Output: 4


# 5. Checking Whether an Item Exists
# - We use the in operator to check whether an item exists in a set.
fruits = {"banana", "orange", "mango", "lemon"}
print("mango" in fruits)    # Output: True
print("apple" in fruits)    # Output: False


# 6. Accessing Items in a Set
# - Sets do not have indexes.
# - We cannot access set items using an index like a list.
# - We usually use a loop to access items in a set.
fruits = {"banana", "orange", "mango", "lemon"}

for fruit in fruits:
    print(fruit)