# 1. Short Hand If-Else
# - A short-hand conditional allows us to write a simple if-elsec condition in one line.

# Syntax:
# code_if_true if condition else code_if_false

age = 20

print("Adult") if age >= 18 else print("Minor")  # Output: Adult


# 2. Nested Conditions
# - A nested condition means using one if statement inside another if statement.
# - Nested conditions are useful when one condition depends on another condition.

# Syntax:
# if condition:
#     if condition:
#         code
#     else:
#         code
# else:
#     code

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed.")  # Output: Entry allowed.
    else:
        print("ID is required.")
else:
    print("You must be 18 or older.")