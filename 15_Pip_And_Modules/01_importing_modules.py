# 1. What is a Module?
# - A module is a Python file containing reusable code.
# - Modules help us organize code and reuse functionality.
# - Data Science libraries provide modules for data analysis.


# 2. Importing a Module
import math

print(math.sqrt(25))
print(math.pi)
# Output:
# 5.0
# 3.141592653589793


# 3. Importing a Specific Function
from math import sqrt

print(sqrt(36))
# Output:
# 6.0


# 4. Importing with an Alias
import statistics as stats

numbers = [10, 20, 30, 40, 50]

print(stats.mean(numbers))
print(stats.median(numbers))
# Output:
# 30
# 30