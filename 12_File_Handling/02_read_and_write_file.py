# Common File Methods in Python:


# 1. read()
# - The read() method reads the complete content of a file and returns it as a string.
with open("data.txt", "r") as file:
    data = file.read()

print(data)


# 2. read(size)
# - The read(size) method reads a specific number of characters from the file.
with open("data.txt", "r") as file:
    data = file.read(10)

print(data)


# 3. readline()
# - The readline() method reads one line from the file.
with open("data.txt", "r") as file:
    line = file.readline()

print(line)


# 4. readlines()
# - The readlines() method reads all lines from the file and returns them as a list.
with open("data.txt", "r") as file:
    lines = file.readlines()

print(lines)


# 5. splitlines()
# - The splitlines() method converts text into a list of lines.
# - It removes the newline character from each line.
with open("data.txt", "r") as file:
    lines = file.read().splitlines()

print(lines)


# 6. write()
# - The write() method writes data to a file.
# - When using "w" mode, existing content is overwritten.
with open("data.txt", "w") as file:
    file.write("Python for Data Science")


# 7. append()
# - The "a" mode adds new content to the end of an existing file.
# - Existing content is not overwritten.
with open("data.txt", "a") as file:
    file.write("\nNumPy")