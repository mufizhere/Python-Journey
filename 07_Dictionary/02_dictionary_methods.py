# Dictionary Methods:


# 1. get() - The get() method is used to access a value using its key.
student = {
    "name": "Mufiz",
    "age": 20
}

print(student.get("name"))             # Output: Mufiz
print(student.get("course"))           # Output: None


# 2. keys() - The keys() method returns all the keys in a dictionary.
student = {
    "name": "Mufiz",
    "age": 20,
    "course": "Data Science"
}

print(student.keys())                  # Output: dict_keys(['name', 'age', 'course'])


# 3. values() - The values() method returns all the values in a dictionary.
student = {
    "name": "Mufiz",
    "age": 20,
    "course": "Data Science"
}

print(student.values())               # Output: dict_values(['Mufiz', 20, 'Data Science'])


# 4. items() - The items() method returns all key-value pairs.
student = {
    "name": "Mufiz",
    "age": 20,
    "course": "Data Science"
}

print(student.items())               # Output: dict_items([('name', 'Mufiz'), ('age', 20), ('course', 'Data Science')])


# 5. update() - The update() method is used to add new items or modify existing items.
student = {
    "name": "Mufiz",
    "age": 20
}

student.update({
    "age": 21,
    "course": "Data Science"
})

print(student)                      # Output: {'name': 'Mufiz', 'age': 21, 'course': 'Data Science'}


# 6. pop() - The pop() method removes an item using its key.
student = {
    "name": "Mufiz",
    "age": 20,
    "course": "Data Science"
}

student.pop("age")
print(student)                        # Output: {'name': 'Mufiz', 'course': 'Data Science'}


# 7. popitem() - The popitem() method removes the last key-value pair.
student = {
    "name": "Mufiz",
    "age": 20,
    "course": "Data Science"
}

student.popitem()
print(student)                       # Output: {'name': 'Mufiz', 'age': 20}


# 8. clear() - The clear() method removes all items from a dictionary.
student = {
    "name": "Mufiz",
    "age": 20
}

student.clear()
print(student)                      # Output: {}


# 9. copy() - The copy() method creates a copy of a dictionary.
student = {
    "name": "Mufiz",
    "age": 20
}

student_copy = student.copy()
print(student_copy)                 # Output: {'name': 'Mufiz', 'age': 20}


# 10. del - The del keyword is used to remove a specific item from a dictionary.
student = {
    "name": "Mufiz",
    "age": 20,
    "course": "Data Science"
}

del student["age"]
print(student)                      # Output: {'name': 'Mufiz', 'course': 'Data Science'}