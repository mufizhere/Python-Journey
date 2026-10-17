# 1. What is JSON?
# - JSON stands for JavaScript Object Notation.
# - JSON is a lightweight format used to store and exchange structured data.
# - JSON data is written using key and value pairs, so it looks similar to a Python dictionary.

# JSON is commonly used for:
# - Storing structured data
# - Working with APIs
# - Exchanging data between applications
# - Storing configuration data
# - Saving data in a readable format

# Example:
person = {
    "name": "Mufiz",
    "age": 20,
    "course": "Data Science"
}

# Important:
# - A Python dictionary and JSON object may look similar, but they are not the same thing.

# Python dictionary:
person = {
    "name": "Mufiz",
    "age": 20
}

print(type(person))
# Output:
# <class 'dict'>


# 2. JSON String to Python Object
# - json.loads() is used to convert a JSON string into a Python object.

import json

person_json = '''
{
    "name": "Mufiz",
    "age": 20,
    "course": "Data Science"
}
'''

person = json.loads(person_json)

print(person)
print(type(person))
print(person["name"])
# Output:
# {'name': 'Mufiz', 'age': 20, 'course': 'Data Science'}
# <class 'dict'>
# Mufiz


# 3. Python Object to JSON String
# - json.dumps() is used to convert a Python object into a JSON string.

person = {
    "name": "Mufiz",
    "age": 20,
    "course": "Data Science"
}

person_json = json.dumps(person, indent=4)
print(person_json)

# indent=4 formats the JSON data with indentation, making it easier to read.
# Output:
# {
#     "name": "Mufiz",
#     "age": 20,
#     "course": "Data Science"
# }


# 4. Saving Python Data into a JSON File
# - json.dump() is used to write a Python object directly into a JSON file.

person = {
    "name": "Mufiz",
    "age": 20,
    "course": "Data Science"
}

with open("student.json", "w") as file:
    json.dump(person, file, indent=4)

# The student.json file will contain:
# {
#     "name": "Mufiz",
#     "age": 20,
#     "course": "Data Science"
# }


# 5. Reading Data from a JSON File
# - json.load() is used to read JSON data from a file and convert it into a Python object.

with open("student.json", "r") as file:
    person = json.load(file)

print(person)
print(type(person))
print(person["name"])


# 6. JSON Methods You Should Remember

# json.loads()
# - Converts JSON string into a Python object.

# json.dumps()
# - Converts a Python object into a JSON string.

# json.load()
# - Reads JSON data from a file and converts it into a Python object.

# json.dump()
# - Converts a Python object and writes it directly into a JSON file.


# 7. Important Difference

# loads() and dumps() work with strings.
# load() and dump() work with files.

# json.loads()   JSON string → Python object
# json.dumps()   Python object → JSON string

# json.load()    JSON file → Python object
# json.dump()    Python object → JSON file