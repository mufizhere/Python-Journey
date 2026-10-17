# 1. What is CSV?
# - CSV stands for Comma-Separated Values.
# - CSV is a file format used to store data in rows and columns.
# - CSV is one of the most common file formats used to store datasets.

# Example:
# Name,Age,Course
# Mufiz,20,Data Science
# Zoro,19,IT
# Alex,21,AI


# 2. Reading a CSV File
# - Python has a built-in csv module for working with CSV files.
import csv

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)

# Output:
# ['Name', 'Age', 'Course']
# ['Mufiz', '20', 'Data Science']
# ['Zoro', '19', 'IT']


# 3. Reading CSV with Header
# - The first row usually contains the column names.
# - We can use next() to skip the header.

with open("students.csv", "r") as file:

    reader = csv.reader(file)
    header = next(reader)

    for row in reader:
        print(row)


# 4. Reading CSV as Dictionary
# - DictReader() reads each row as a dictionary.

with open("students.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row["Name"])
        print(row["Course"])


# 5. Writing Data to a CSV File
# - We can use csv.writer() to write data into a CSV file.

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])
    writer.writerow(["Mufiz", 20, "Data Science"])
    writer.writerow(["Zoro", 19, "IT"])


# 6. Important Methods to Remember

# csv.reader()
# - Reads CSV data row by row.

# csv.DictReader()
# - Reads CSV data as dictionaries.

# csv.writer()
# - Writes data into a CSV file.

# pd.read_csv()
# - Reads a CSV file into a Pandas DataFrame.