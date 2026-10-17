# List Methods:


# 1. append() -> Adds an item to the end of the list.
fruits = ["banana", "orange", "mango"]
fruits.append("lemon")
print(fruits)               # Output: ['banana', 'orange', 'mango', 'lemon']


# 2. insert() -> Adds an item at a specific index.
fruits = ["banana", "orange", "mango"]
fruits.insert(1, "apple")
print(fruits)               # Output: ['banana', 'apple', 'orange', 'mango']


# 3. remove() -> Removes the first matching item from the list.
fruits = ["banana", "orange", "mango", "lemon"]
fruits.remove("orange")
print(fruits)               # Output: ['banana', 'mango', 'lemon']


# 4. pop() -> Removes and returns an item from the list.
fruits = ["banana", "orange", "mango", "lemon"]
fruits.pop()
print(fruits)               # Output: ['banana', 'orange', 'mango']

# pop(index) removes an item from a specific position.
fruits = ["banana", "orange", "mango", "lemon"]
fruits.pop(1)
print(fruits)               # Output: ['banana', 'mango', 'lemon']


# 5. clear() -> Removes all items from the list.
fruits = ["banana", "orange", "mango"]
fruits.clear()
print(fruits)               # Output: []


# 6. copy() -> Creates a copy of the list.
fruits = ["banana", "orange", "mango"]
fruits_copy = fruits.copy()
print(fruits_copy)          # Output: ['banana', 'orange', 'mango']


# 7. extend() -> Adds multiple items from another list.
fruits = ["banana", "orange"]
vegetables = ["tomato", "potato"]
fruits.extend(vegetables)
print(fruits)               # Output: ['banana', 'orange', 'tomato', 'potato']


# 8. count() -> Counts how many times an item appears.
numbers = [1, 2, 2, 3, 2, 4]
print(numbers.count(2))     # Output: 3


# 9. index() -> Returns the index of the first matching item.
fruits = ["banana", "orange", "mango", "lemon"]
print(fruits.index("mango"))    # Output: 2


# 10. reverse() -> Reverses the order of items in the list.
fruits = ["banana", "orange", "mango", "lemon"]
fruits.reverse()
print(fruits)                   # Output: ['lemon', 'mango', 'orange', 'banana']


# 11. sort() -> Sorts the list in ascending order.
numbers = [5, 2, 8, 1, 3]
numbers.sort()
print(numbers)                  # Output: [1, 2, 3, 5, 8]

# Sorting in descending order
numbers = [5, 2, 8, 1, 3]
numbers.sort(reverse=True)
print(numbers)                  # Output: [8, 5, 3, 2, 1]