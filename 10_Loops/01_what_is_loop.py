# 1. What are Loops?
# - Loops are used to execute the same block of code repeatedly.
# - Python provides two main types of loops:
    # - 1. while loop
    # - 2. for loop


# 2. Why Do We Use Loops?
# - Loops reduce code repetition.
# - They help execute a task multiple times.
# - They make code shorter and easier to maintain.

# Without a Loop:
print("Hello")
print("Hello")
print("Hello")

# With a Loop:
for i in range(3):
    print("Hello")


# 3. Types of Loops
# - while loop:
#   Repeats code as long as a condition is True.

# - for loop:
#   Iterates over a sequence or iterable.


# Example of While Loop:
count = 0

while count < 3:
    print(count)
    count += 1
# Output:
# 0
# 1
# 2

# Example of For Loop:
for number in range(1, 4):
    print(number)
# Output:
# 1
# 2
# 3