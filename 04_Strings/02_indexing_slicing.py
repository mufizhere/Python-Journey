# 1. What is String Indexing?
# - String indexing is used to access individual characters from a string using their position.
# - Python uses zero-based indexing.
# - This means the first character has index 0.

language = "Python"

print(language[0])  # P
print(language[1])  # y
print(language[2])  # t
print(language[3])  # h
print(language[4])  # o
print(language[5])  # n


# 2. Positive Indexing
# - Positive indexing starts from the left side.
# - The first character starts with index 0.

language = "Python"

print(language[0])  # P
print(language[3])  # h
print(language[5])  # n


# 3. Negative Indexing
# - Negative indexing starts from the right side.
# - The last character has index -1.

language = "Python"

print(language[-1])  # n
print(language[-2])  # o
print(language[-3])  # h



# 4. What is String Slicing?
# - String slicing is used to extract a part of a string.

# Syntax:
# string[start:end]
# - The start index is included.
# - The end index is not included.

language = "Python"

print(language[0:3])  # Pyt
print(language[1:4])  # yth
print(language[2:6])  # thon


# Slicing From the Beginning:
# - If the start index is not specified,
# - Python starts from index 0.
language = "Python"

print(language[:3])  # Pyt
print(language[:4])  # Pyth


# Slicing Until the End:
# - If the end index is not specified,
# - Python continues until the end of the string.
language = "Python"

print(language[3:])  # hon
print(language[2:])  # thon


# Slicing With Negative Index
language = "Python"
print(language[-3:])  # hon
print(language[-4:])  # thon


# Slicing With Start and End Index:
language = "Python"
print(language[1:5])  # ytho


# 5. Slicing With Step

# Syntax:
# string[start:end:step]
# - Step controls how many characters Python skips.

language = "Python"

print(language[0:6:1])  # Python
print(language[0:6:2])  # Pto
print(language[0:6:3])  # Ph


# Reverse a String:
# A step of -1 reads the string from right to left.

language = "Python"
print(language[::-1])  # nohtyP