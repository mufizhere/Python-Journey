# 4. Conditions with Data Structures
# - We can use if conditions to check values stored inside data structures.
# - This is very common in Data Science when filtering or checking data.


# Example 1: Condition with a List
marks = [45, 78, 90, 32, 65]

for mark in marks:
    if mark >= 50:
        print(mark, "Pass")
    else:
        print(mark, "Fail")

# Output:
# 45 Fail
# 78 Pass
# 90 Pass
# 32 Fail
# 65 Pass



# Example 2: Condition with a Dictionary
student = {
    "name": "Mufiz",
    "age": 20,
    "marks": 85
}

if student["marks"] >= 50:
    print(student["name"], "has passed.")  # Output: Mufiz has passed.
else:
    print(student["name"], "has failed.")



# Example 3: Condition with a Set
numbers = {10, 20, 30, 40, 50}

if 30 in numbers:
    print("30 is present in the set.")  # Output: 30 is present in the set.
else:
    print("30 is not present in the set.")



# Example 4: Condition with a List of Dictionaries
students = [
    {"name": "Mufiz", "marks": 85},
    {"name": "Zoro", "marks": 45},
    {"name": "Ali", "marks": 72}
]

for student in students:
    if student["marks"] >= 50:
        print(student["name"], "Pass")
    else:
        print(student["name"], "Fail")

# Output:
# Mufiz Pass
# Zoro Fail
# Ali Pass