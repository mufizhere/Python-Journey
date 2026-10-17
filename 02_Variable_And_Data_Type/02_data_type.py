# 1. What is a Data Type?
# A data type defines the kind of value stored in a variable.
# It tells Python how the value should be handled.


# 2. Checking the Data Type
# The type() function is used to check the data type of a value.

age = 20
print(type(age))

# - Python has 8 commonly used built-in data types:
# int    - Integer numbers
# float  - Decimal numbers
# str    - Text
# bool   - True or False
# list   - Ordered and changeable collection
# tuple  - Ordered and unchangeable collection
# dict   - Key-value pairs
# set    - Unordered collection of unique values


# 3. Integer (int)
# - int is used to store whole numbers without decimal values.
age = 20
marks = 85
print(age)
print(type(age))


# 4. Float (float)
# - float is used to store numbers with decimal values.
percentage = 69.11
height = 5.8
print(percentage)
print(type(percentage))


# 5. String (str)
# - str is used to store text. Strings are written inside single or double quotes.
name = "Mufiz"
message = "Welcome to Python"
print(name)
print(type(name))


# 6. Boolean (bool)
# - bool stores one of two values: True or False
is_student = True
is_passed = False
print(is_student)
print(type(is_student))


# 7. List (list)
# - A list stores multiple values in an ordered collection. Lists are changeable.
my_list = [11, "Mufiz", 69.11, None]
print(my_list)
print(type(my_list))


# 8. Tuple (tuple)
# - A tuple stores multiple values in an ordered collection.
# - Tuples cannot be changed after they are created.
my_tuple = ("Mufiz", 20, True)
print(my_tuple)
print(type(my_tuple))


# 9. Dictionary (dict)
# - A dictionary stores data in key-value pairs.
my_dict = {
    "name": "Mufiz",
    "age": 20,
    "is_passed": True
}
print(my_dict)
print(type(my_dict))


# 10. Set (set)
# - A set stores unique values.
# - Sets are unordered collections.
my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))


# Key Points to Remember:
    # 1. A data type defines the kind of value stored in a variable.
    # 2. The type() function is used to check a data type.
    # 3. int is used for whole numbers.
    # 4. float is used for decimal numbers.
    # 5. str is used for text.
    # 6. bool stores True or False.
    # 7. list is ordered and changeable.
    # 8. tuple is ordered and unchangeable.
    # 9. dict stores data as key-value pairs.
    # 10. set stores unique values.
