# Tuple Methods and Operations


# 1. count() -> Counts how many times an item appears in a tuple.
numbers = (1, 2, 2, 3, 2, 4)
print(numbers.count(2))                 # Output: 3


# 2. index() -> Returns the index of the first occurrence of an item.
fruits = ("banana", "orange", "mango", "lemon")
print(fruits.index("mango"))            # Output: 2


# 3. + Operator -> Joins two or more tuples.
fruits = ("banana", "orange", "mango")
vegetables = ("tomato", "potato")

result = fruits + vegetables
print(result)                 # Output: ('banana', 'orange', 'mango', 'tomato', 'potato')


# 4. * Operator -> Repeats the items in a tuple.
numbers = (1, 2, 3)
result = numbers * 2
print(result)               # Output: (1, 2, 3, 1, 2, 3)


# 5. list() -> Converts a tuple into a list.
fruits = ("banana", "orange", "mango")
fruits_list = list(fruits)
print(fruits_list)          # Output: ['banana', 'orange', 'mango']


# Modifying a Tuple by Converting It to a List
fruits = ("banana", "orange", "mango")

fruits_list = list(fruits)
fruits_list[0] = "apple"

fruits = tuple(fruits_list)
print(fruits)               # Output: ('apple', 'orange', 'mango')


# 6. tuple() -> Converts a list into a tuple.
fruits_list = ["banana", "orange", "mango"]
fruits = tuple(fruits_list)
print(fruits)               # Output: ('banana', 'orange', 'mango')


# 7. del -> Deletes the entire tuple.\
fruits = ("banana", "orange", "mango")
del fruits
# print(fruits)
# This gives:
# NameError: name 'fruits' is not defined