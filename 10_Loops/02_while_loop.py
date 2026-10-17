# 1. What is a While Loop?
# - A while loop executes a block of code as long as its condition is True.
# - The loop stops when the condition becomes False.


# 2. Syntax of While Loop
# while condition:
#     code


# 3. Basic While Loop

count = 0
while count < 5:
    print(count)
    count += 1
# Output:
# 0
# 1
# 2
# 3
# 4


# 4. While Loop with Else
# - The else block executes when the while loop finishes normally.
# - The else block does not execute if the loop is terminated by break.

count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop ended.")
# Output:
# 0
# 1
# 2
# Loop ended.


# 5. Break Statement
# - break stops the loop immediately.
# - It is used when we want to terminate a loop before it finishes normally.

count = 0
while count < 5:
    print(count)
    count += 1

    if count == 3:
        break
# Output:
# 0
# 1
# 2


# 6. Continue Statement
# - continue skips the current iteration.
# - The loop then continues with the next iteration.

count = 0
while count < 5:
    if count == 3:
        count += 1
        continue

    print(count)
    count += 1
# Output:
# 0
# 1
# 2
# 4


# 7. Important Note
# - Always update the loop variable when necessary.
# - Otherwise, the condition may remain True and create an infinite loop.