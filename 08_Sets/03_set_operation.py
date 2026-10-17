# 1. What are Set Operations?
# - Set operations are used to compare and combine sets.

# - Common set operations are:
#   Union
#   Intersection
#   Difference
#   Symmetric Difference
#   Subset
#   Superset
#   Disjoint


# 2. Union - Union combines all unique items from two sets.
# - We can use union() or |.
fruits = {"banana", "orange", "mango"}
vegetables = {"tomato", "potato", "onion"}

result = fruits.union(vegetables)
print(result)           # Output: {'banana', 'orange', 'mango', 'tomato', 'potato', 'onion'}

# Using the | operator
result = fruits | vegetables
print(result)           # Output: {'banana', 'orange', 'mango', 'tomato', 'potato', 'onion'}


# 3. Intersection - Intersection returns the items that exist in both sets.
numbers = {1, 2, 3, 4, 5}
even_numbers = {2, 4, 6, 8}

result = numbers.intersection(even_numbers)
print(result)       # Output: {2, 4}

# Using the & operator
result = numbers & even_numbers
print(result)       # Output: {2, 4}


# 4. Difference - Difference returns the items that exist in the first set but do not exist in the second set.
numbers = {1, 2, 3, 4, 5}
even_numbers = {2, 4, 6, 8}

result = numbers.difference(even_numbers)
print(result)   # Output: {1, 3}

# Using the - operator
result = numbers - even_numbers
print(result)   # Output: {1, 3}


# 5. Symmetric Difference - Symmetric difference returns items that are in either set, but not in both sets.
numbers = {1, 2, 3, 4}
other_numbers = {3, 4, 5, 6}

result = numbers.symmetric_difference(other_numbers)
print(result)       # Output: {1, 2, 5, 6}

# Using the ^ operator
result = numbers ^ other_numbers
print(result)       # Output: {1, 2, 5, 6}


# 6. Subset - A set is a subset when all of its items exist inside another set.
numbers = {1, 2, 3, 4, 5}
small_numbers = {1, 2, 3}
print(small_numbers.issubset(numbers))      # Output: True


# 7. Superset - A set is a superset when it contains all items of another set.
numbers = {1, 2, 3, 4, 5}
small_numbers = {1, 2, 3}
print(numbers.issuperset(small_numbers))        # Output: True


# 8. Disjoint Sets - Two sets are disjoint when they have no common items.

even_numbers = {2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7}
print(even_numbers.isdisjoint(odd_numbers))     # Output: True

# Example with Common Items
python = {"p", "y", "t", "h", "o", "n"}
dragon = {"d", "r", "a", "g", "o", "n"}

print(python.isdisjoint(dragon))                # Output: False