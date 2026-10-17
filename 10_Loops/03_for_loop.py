# 1. What is a For Loop?
# - A for loop is used to iterate over a sequence or iterable.
# - It can iterate over lists, tuples, strings, and ranges.


# 2. Syntax of For Loop
# for variable in sequence:
#     code


# 3. For Loop with a List
fruits = ["banana", "orange", "mango", "lemon"]

for fruit in fruits:
    print(fruit)
# Output:
# banana
# orange
# mango
# lemon


# 4. For Loop with Range
# - The range() function generates a sequence of numbers.
# - The stop value is excluded.

for number in range(1, 6):
    print(number)
# Output:
# 1
# 2
# 3
# 4
# 5


# 5. For Loop with Else
# - The else block executes when the for loop finishes normally.
# - The else block does not execute if the loop is terminated by break.

for number in range(1, 4):
    print(number)
else:
    print("Loop ended.")
# Output:
# 1
# 2
# 3
# Loop ended.


# 6. Break Statement
# - break terminates the loop immediately.

for number in range(1, 6):
    if number == 4:
        break
    print(number)
# Output:
# 1
# 2
# 3


# 7. Continue Statement
# - continue skips the current iteration and moves to the next iteration.

for number in range(1, 6):
    if number == 3:
        continue

    print(number)
# Output:
# 1
# 2
# 4
# 5


# 8. Nested For Loop
# - A nested loop is a loop inside another loop.

for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)
# Output:
# 1 1
# 1 2
# 2 1
# 2 2