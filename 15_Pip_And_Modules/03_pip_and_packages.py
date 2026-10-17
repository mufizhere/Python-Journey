# 1. What is pip?
# - pip is a tool used to install Python packages.
# - Packages provide reusable code and additional functionality.
# - Data Scientists use packages such as NumPy, Pandas, and Matplotlib.

# 2. What is a Package?
# - A package is a collection of Python modules that provide related functionality.
# - Packages help us reuse existing code instead of writing everything from scratch.
# - Examples: NumPy, Pandas, Matplotlib, Seaborn, and Scikit-learn.

# 3. Installing Data Science Libraries
# - Open the VS Code terminal to install Python libraries.
# - Run the following command in the terminal:

# python -m pip install numpy pandas matplotlib seaborn scikit-learn

# - NumPy is used for numerical computing and array operations.
# - Pandas is used for data manipulation and analysis.
# - Matplotlib is used for data visualization.
# - Seaborn is used for statistical data visualization.
# - Scikit-learn is used for machine learning.

# Important:
# - Run the installation command in the terminal, not inside a Python file.
# - If you use a virtual environment, activate it before installing packages.
# - This ensures that the packages are installed in the correct environment.

# 4. Importing Installed Libraries
# - After installing a package, import it into your Python file to use its functionality.
# - The import statement makes the package available in your Python program.
#
# Example:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

# - np is the commonly used alias for NumPy.
# - pd is the commonly used alias for Pandas.
# - plt is the commonly used alias for Matplotlib's pyplot module.
# - sns is the commonly used alias for Seaborn.
# - sklearn is the import name for Scikit-learn.


# 1. Importing NumPy
# - NumPy is used for numerical computing and arrays.
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])
print(np.mean(numbers))

# Output:
# 30.0


# 2. Importing Pandas
# - Pandas is used for data manipulation and analysis.
import pandas as pd

data = {
    "Car": ["Toyota", "Honda", "BMW"],
    "Price": [1200000, 900000, 7500000]
}

df = pd.DataFrame(data)
print(df)

# Output:
#       Car    Price
# 0  Toyota  1200000
# 1   Honda   900000
# 2     BMW  7500000


# 3. Importing Matplotlib
# - Matplotlib is used for data visualization.
import matplotlib.pyplot as plt

print("Matplotlib imported successfully.")
# Output:
# Matplotlib imported successfully.


# 4. Importing Seaborn
# - Seaborn helps create statistical visualizations.
import seaborn as sns

print("Seaborn imported successfully.")

# Output:
# Seaborn imported successfully.


# 5. Importing Scikit-learn
# - Scikit-learn provides tools for machine learning.
import sklearn

print("Scikit-learn imported successfully.")

# Output:
# Scikit-learn imported successfully.