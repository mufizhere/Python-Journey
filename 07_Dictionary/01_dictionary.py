# 1. What is a Dictionary?
# - A dictionary is a collection of data stored in key-value pairs.
# - Each item in a dictionary has a key and a value.
# - Dictionaries are ordered and changeable.
# - Dictionaries are written using curly brackets {}.

student = {
    "name": "Mufiz",
    "age": 20,
    "course": "Data Science"
}
print(student)          # Output: {'name': 'Mufiz', 'age': 20, 'course': 'Data Science'}

# Dictionary Structure:
# "name"   -> Key
# "Mufiz"  -> Value
# "age"    -> Key
# 20       -> Value


# 2. Creating an Empty Dictionary
empty_dict = {}

print(empty_dict)       # Output: {}
print(len(empty_dict))  # Output: 0

# A Dictionary Can Contain Different Data Types:
student = {
    "name": "Mufiz",
    "age": 20,
    "marks": 85.5,
    "is_student": True
}

print(student)          # Output: {'name': 'Mufiz', 'age': 20, 'marks': 85.5, 'is_student': True}


# 3. Finding the Length of a Dictionary
student = {
    "name": "Mufiz",
    "age": 20,
    "course": "Data Science"
}

print(len(student))     # Output: 3


# 4. Accessing Dictionary Values
# - We can access a value by using its key.
student = {
    "name": "Mufiz",
    "age": 20,
    "course": "Data Science"
}

print(student["name"])      # Output: Mufiz
print(student["age"])       # Output: 20
print(student["course"])    # Output: Data Science


# 5. Accessing Values Using get()
# - The get() method is used to access a value using its key.
# - If the key does not exist, get() returns None instead of an error.
student = {
    "name": "Mufiz",
    "age": 20
}

print(student.get("name"))          # Output: Mufiz
print(student.get("course"))        # Output: None


# 6. Adding Items to a Dictionary
# - We can add a new key-value pair to a dictionary.
student = {
    "name": "Mufiz",
    "age": 20
}

student["course"] = "Data Science"
print(student)          # Output: {'name': 'Mufiz', 'age': 20, 'course': 'Data Science'}


# 7. Modifying Items in a Dictionary
# - We can change the value of an existing key.
student = {
    "name": "Mufiz",
    "age": 20,
    "course": "Data Science"
}

student["age"] = 21
print(student)      # Output: {'name': 'Mufiz', 'age': 21, 'course': 'Data Science'}


# 8. Checking Whether a Key Exists
student = {
    "name": "Mufiz",
    "age": 20,
    "course": "Data Science"
}

print("name" in student)        # Output: True
print("city" in student)        # Output: False