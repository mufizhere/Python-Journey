# Tuple Indexing and Slicing:


# 1. Positive Indexing

# - Tuple indexing starts from 0.
fruits = ("banana", "orange", "mango", "lemon")

print(fruits[0])        # Output: banana
print(fruits[1])        # Output: orange
print(fruits[2])        # Output: mango
print(fruits[3])        # Output: lemon


# 2. Negative Indexing

# - Negative indexing starts from -1 from the right side.
fruits = ("banana", "orange", "mango", "lemon")

print(fruits[-1])       # Output: lemon
print(fruits[-2])       # Output: mango
print(fruits[-3])       # Output: orange


# - Finding the Last Item Using len()
fruits = ("banana", "orange", "mango", "lemon")
last_index = len(fruits) - 1

print(fruits[last_index])       # Output: lemon


# 2. Tuple Slicing

# Syntax:
# tuple[start:end]
# - The start index is included.
# - The end index is not included.
fruits = ("banana", "orange", "mango", "lemon")

print(fruits[0:2])          # Output: ('banana', 'orange')
print(fruits[1:3])          # Output: ('orange', 'mango')


# - Slicing From the Beginning
fruits = ("banana", "orange", "mango", "lemon")
print(fruits[:3])           # Output: ('banana', 'orange', 'mango')

# - Slicing Until the End
fruits = ("banana", "orange", "mango", "lemon")
print(fruits[1:])           # Output: ('orange', 'mango', 'lemon')

# - Slicing Using Negative Index
fruits = ("banana", "orange", "mango", "lemon")
print(fruits[-3:])          # Output: ('orange', 'mango', 'lemon')
print(fruits[-3:-1])        # Output: ('orange', 'mango')


# 3. Slicing With Step

# Syntax:
# Tuple[start:end:step]
# - Step controls how many item Python skips.

numbers = (1, 2, 3, 4, 5, 6)
print(numbers[0:6:2])       # Output: (1, 3, 5)

# Reverse a Tuple Using Slicing
numbers = (1, 2, 3, 4, 5)
print(numbers[::-1])        # Output: (5, 4, 3, 2, 1)