# String Methods:


# 1. lower() -> Converts all characters to lowercase.
text = "Python Programming"
print(text.lower())         # Output: python programming


# 2. upper() -> Converts all characters to uppercase.
text = "Python Programming"
print(text.upper())         # Output: PYTHON PROGRAMMING


# 3. capitalize() -> Converts the first character to uppercase.
text = "python programming"
print(text.capitalize())    # Output: Python programming


# 4. title() -> Converts the first character of each word to uppercase.
text = "python programming language"
print(text.title())         # Output: Python Programming Language


# 5. strip() -> Removes spaces from both the beginning and end.
text = "  Python Programming  "
print(text.strip())         # Output: Python Programming


# 6. replace() -> Replaces a specified value with another value.
text = "I love Java"
print(text.replace("Java", "Python"))  # Output: I love Python


# 7. split() -> Splits a string into a list.
text = "Python is easy"
print(text.split())         # Output: ['Python', 'is', 'easy']


# 8. join() -> Joins elements of a list into a single string.
words = ["Python", "is", "easy"]
print(" ".join(words))      # Output: Python is easy


# 9. find() -> Returns the index of the first occurrence of a value.
text = "Python Programming"
print(text.find("Pro"))     # Output: 7


# 10. count() -> Counts how many times a value occurs in a string.
text = "Python Programming"
print(text.count("P"))      # Output: 2


# 11. startswith() -> Checks whether a string starts with a specified value.
text = "Python Programming"
print(text.startswith("Python"))  # Output: True


# 12. endswith() -> Checks whether a string ends with a specified value.
text = "Python Programming"
print(text.endswith("Programming"))  # Output: True


# 13. isalpha() -> Checks whether all characters are alphabets.
text = "Python"
print(text.isalpha())       # Output: True


# 14. isdigit() -> Checks whether all characters are digits.
text = "12345"
print(text.isdigit())       # Output: True


# 15. isalnum() -> Checks whether all characters are letters or numbers.
text = "Python123"
print(text.isalnum())       # Output: True