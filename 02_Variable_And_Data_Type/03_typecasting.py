# 1. What is Type Casting?
# - Type casting is the process of converting a value from one data type to another data type.
# - Python provides built-in functions such as:
# - int(), float(), str(), bool(), list(), tuple(), and set()


# 2. Common Type Conversions:
# str   -> int      "10"     -> 10
# str   -> float    "10.5"   -> 10.5
# int   -> float    10       -> 10.0
# float -> int      10.5     -> 10
# int   -> str      10       -> "10"
# float -> str      10.5     -> "10.5"
# int   -> bool     1        -> True
# bool  -> int      True     -> 1


# 3. String to Integer (str -> int)
age = "20"
print(age, ":", type(age))

age = int(age)
print(age, ":", type(age))


# 4. String to Float (str -> float)
price = "99.50"
print(price, ":", type(price))

price = float(price)
print(price, ":", type(price))


# 5. Integer to Float (int -> float)
age = 20
print(age, ":", type(age))
age = float(age)
print(age, ":", type(age))


# 6. Float to Integer (float -> int)
price = 99.50
print(price, ":", type(price))

price = int(price)
print(price, ":", type(price))
# Note:
# - Converting a float to an integer removes the decimal part.
# - Example: 99.50 becomes 99


# 7. Integer to String (int -> str)
age = 20
print(age, ":", type(age))

age = str(age)
print(age, ":", type(age))


# 8. Float to String (float -> str)
price = 99.50
print(price, ":", type(price))

price = str(price)
print(price, ":", type(price))


# 9. Integer to Boolean (int -> bool)
number = 1
print(number, ":", type(number))

number = bool(number)
print(number, ":", type(number))
# Note:
# -  0 becomes False.
# - Any non-zero integer becomes True.


# 10. Boolean to Integer (bool -> int)
status = True
print(status, ":", type(status))

status = int(status)
print(status, ":", type(status))
# Note:
# - True becomes 1.
# - False becomes 0.


# 11. List to Tuple (list -> tuple)
data = [10, 20, 30]
print(data, ":", type(data))

data = tuple(data)
print(data, ":", type(data))


# 12. Tuple to List (tuple -> list)
data = (10, 20, 30)
print(data, ":", type(data))

data = list(data)
print(data, ":", type(data))


# 13. List to Set (list -> set)
data = [10, 20, 20, 30]
print(data, ":", type(data))

data = set(data)
print(data, ":", type(data))
# Note:
# - A set stores only unique values.
# - Therefore, the duplicate 20 is removed.


# Key Points to Remember:
    # 1. Type casting converts a value from one data type to another.
    # 2. int() converts a value to an integer.
    # 3. float() converts a value to a floating-point number.
    # 4. str() converts a value to a string.
    # 5. bool() converts a value to True or False.
    # 6. list() converts an iterable into a list.
    # 7. tuple() converts an iterable into a tuple.
    # 8. set() converts an iterable into a set of unique values.
    # 9. Converting float to int removes the decimal part.
    # 10. Not every value can be converted successfully.