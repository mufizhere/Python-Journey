# Set Methods:


# 1. add() - The add() method is used to add one item to a set.
fruits = {"banana", "orange", "mango", "lemon"}
fruits.add("lime")
print(fruits)                   # Output: {'banana', 'orange', 'mango', 'lemon', 'lime'}


# 2. update() - The update() method is used to add multiple items to a set.
fruits = {"banana", "orange", "mango", "lemon"}
fruits.update(["lime", "apple", "grapes"])
print(fruits)                   # Output: {'banana', 'orange', 'mango', 'lemon', 'lime', 'apple', 'grapes'}


# 3. remove() - The remove() method removes a specific item from a set.
# - If the item does not exist, remove() gives an error.
fruits = {"banana", "orange", "mango", "lemon"}
fruits.remove("orange")
print(fruits)                   # Output: {'banana', 'mango', 'lemon'}


# 4. discard() - The discard() method removes a specific item.
# - If the item does not exist, discard() does not give an error.
fruits = {"banana", "orange", "mango", "lemon"}
fruits.discard("apple")
print(fruits)                   # Output: {'banana', 'orange', 'mango', 'lemon'}


# 5. pop() - The pop() method removes and returns an item from a set.
# - Because sets are unordered, we cannot know which item will be removed.
fruits = {"banana", "orange", "mango", "lemon"}
removed_item = fruits.pop()
print(removed_item)
print(fruits)


# 6. clear() - The clear() method removes all items from a set.
fruits = {"banana", "orange", "mango", "lemon"}
fruits.clear()
print(fruits)   # Output: set()


# 7. del - The del keyword deletes the complete set.
fruits = {"banana", "orange", "mango", "lemon"}
del fruits


# 8. Converting a List to a Set
# - We can convert a list into a set using set().
# - Converting a list to a set removes duplicate values.
fruits = ["banana", "orange", "mango", "lemon", "orange", "banana"]
fruits = set(fruits)
print(fruits)       # Output: {'banana', 'orange', 'mango', 'lemon'}