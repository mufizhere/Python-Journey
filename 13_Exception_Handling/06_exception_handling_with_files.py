# 1. Exception Handling with Files
# - File operations can cause different exceptions.
# - Common file exceptions include:
    # FileNotFoundError
    # PermissionError
    # IsADirectoryError


# 2. Handling FileNotFoundError
try:
    with open("data.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("The file does not exist.")


# 3. Reading a File Safely
try:
    with open("students.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("students.txt was not found.")

except PermissionError:
    print("You do not have permission to access this file.")


# 4. Writing to a File Safely
try:
    with open("students.txt", "w") as file:
        file.write("Mufiz, Data Science")
        print("Data saved successfully.")

except PermissionError:
    print("You do not have permission to write to this file.")


# 5. Using finally with Files
file = None

try:
    file = open("data.txt", "r")
    data = file.read()
    print(data)

except FileNotFoundError:
    print("File not found.")

finally:
    if file is not None:
        file.close()
        print("File closed.")


# 6. Recommended Method
# - The with open() method is recommended for file handling.
# - It automatically closes the file.
# - This makes the code safer and cleaner.
try:
    with open("data.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("File not found.")


# 7. Data Science Connection
# - Exception handling is important in Data Science.
# - It can help handle:
# - Missing files
# - Invalid CSV data
# - Invalid user input
# - Incorrect data types
# - Database errors
# - Data processing errors