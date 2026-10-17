# 1. What is a String?
# - A string is a sequence of characters used to store text.
# - Strings can be written using single quotes (' ') or double quotes (" ").

# Example:
letter = 'P'
print(letter)

greeting = "Hello, World!"
print(greeting)

sentence = "I hope you are enjoying Python."
print(sentence)


# 2. Multiline String:
# - A multiline string is used to store text that contains multiple lines.
# - Triple single quotes or triple double quotes can be used.

# Example:
multiline_string = """
I am learning Python.
Python is useful for Data Science.
I am practicing Python every day.
"""
print(multiline_string)


# 3. Length of a String:
# - The len() function returns the number of characters in a string.

letter = "P"
greeting = "Hello, World!"

print(len(letter))
print(len(greeting))


# 4. String Concatenation:
# - String concatenation means joining two or more strings together.
# - The + operator is used to concatenate strings.

first_name = "Mufiz"
last_name = "Parasara"

full_name = first_name + " " + last_name
print(full_name)


# 5. Unpacking Characters:
# String unpacking means assigning each character of a string to a separate variable.

language = "Python"
a, b, c, d, e, f = language

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


# 6. String Formatting Using format():
# - The format() method is used to insert values into a string.

first_name = "Mufiz"
last_name = "Parasara"
course = "Data Science"
city = "Rajkot"

sentence = "I am {} {}. I am studying {}. I live in {}.".format(first_name, last_name, course, city)
print(sentence)


# 7. String Formatting Using f-Strings:
# - f-strings provide a simple and readable way to insert variables and expressions directly into a string.

first_name = "Mufiz"
last_name = "Parasara"
course = "Data Science"
city = "Rajkot"

sentence = f"I am {first_name} {last_name}. I am studying {course}. I live in {city}."
print(sentence)