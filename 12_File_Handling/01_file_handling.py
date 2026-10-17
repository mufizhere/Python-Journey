# 1. What is File Handling?
# - File handling is the process of working with files using Python.
# - It allows us to create, read, write, update, and manage files.
# - In Data Science, file handling is important because data is often stored in files and needs to be loaded, processed, and saved.


# 2. Why is File Handling Important?
# - Data can be stored in different types of files depending on the application and purpose.
# - File handling allows Python to access and work with this data.

# Common file types used in Data Science include:
# .txt   Text files
# .csv   Comma-separated values files
# .json  JSON files
# .xlsx  Excel files
# .xml   XML files


# 3. open() Function
# - The open() function is used to open a file in Python.
# - close() is used to close the file after completing the operation.

# Example:
file = open("data.txt", "r")
print(file)
file.close()


# 4. File Modes
# - File modes define how Python should work with a file.

# r = Read
# w = Write
# a = Append
# x = Create
# t = Text
# b = Binary

# Example of Reading a File:
file = open("data.txt", "r")
data = file.read()
print(data)
file.close()


# 5. with open()
# - The with open() statement is the recommended way to work with files.
# - It automatically closes the file when the code inside the with block has finished executing.
# - This makes the code cleaner, safer, and easier to manage.

# Example:
with open("data.txt", "r") as file:
    data = file.read()

print(data)
# The file is automatically closed after the with block.