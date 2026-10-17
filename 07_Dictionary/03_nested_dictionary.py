# 1. What is a Nested Dictionary?
# - A nested dictionary is a dictionary that contains another dictionary as a value.

students = {
    "student1": {
        "name": "Mufiz",
        "age": 20,
        "course": "Data Science"
    },
    "student2": {
        "name": "Zoro",
        "age": 19,
        "course": "IT"
    }
}

print(students)


# 2. Accessing Values from a Nested Dictionary
# - We can access values from a nested dictionary by using multiple keys.

students = {
    "student1": {
        "name": "Mufiz",
        "age": 20,
        "course": "Data Science"
    }
}

print(students["student1"]["name"])         # Output: Mufiz
print(students["student1"]["age"])          # Output: 20
print(students["student1"]["course"])       # Output: Data Science


# 3. Modifying Values in a Nested Dictionary
students = {
    "student1": {
        "name": "Mufiz",
        "age": 20,
        "course": "Data Science"
    }
}

students["student1"]["age"] = 21
print(students)                             # Output: {'student1': {'name': 'Mufiz', 'age': 21, 'course': 'Data Science'}}


# 4. Adding Items to a Nested Dictionary
students = {
    "student1": {
        "name": "Mufiz",
        "age": 20
    }
}

students["student1"]["course"] = "Data Science"
print(students)                             # Output: {'student1': {'name': 'Mufiz', 'age': 20, 'course': 'Data Science'}}


# 5. Dictionary Containing a List
# - A dictionary can contain a list as a value.
student = {
    "name": "Mufiz",
    "age": 20,
    "skills": ["Python", "NumPy", "Pandas"]
}

print(student["skills"])                    # Output: ['Python', 'NumPy', 'Pandas']
print(student["skills"][0])                 # Output: Python


# 6. Nested Dictionary for Multiple Students
students = {
    "student1": {
        "name": "Mufiz",
        "age": 20,
        "marks": 85
    },
    "student2": {
        "name": "Zoro",
        "age": 19,
        "marks": 90
    }
}

print(students["student1"]["marks"])        # Output: 85
print(students["student2"]["marks"])        # Output: 90