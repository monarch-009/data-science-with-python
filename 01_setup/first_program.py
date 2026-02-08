# Single-line comment

"""
This is a multi-line comment (docstring style).
You can write several lines of explanation here.
Python will completely ignore everything inside triple quotes
when it's used like this (not assigned to a variable).
"""

# BASIC PRINT STATEMENTS

print("Hello, Python world!")           # simple string
print('Single quotes work too')         # single quotes are also fine
print(2026)                             # printing a number
print("Python", "is", "fun")            # multiple arguments = spaces between

# f-strings (formatted string literals) → best way since Python 3.6

name = "Aditya Singh"
age = 23
height = 198
is_student = True

# Basic f-string
print(f"My name is {name}.")

# Multiple variables + expressions
print(f"{name} is {age} years old and {height} meters tall.")

# You can do calculations inside {}
print(f"Next year {name} will be {age + 1} years old.")

# Boolean values
print(f"Is {name} a student? → {is_student}")

# Formatting numbers
print(f"Height with 2 decimal places: {height:.2f} cm")
print(f"Age with leading zero: {age:03d}")


# Older ways of formatting (you might see in older code)


# % formatting (old style - still works but not recommended)
print("Hello, %s! You are %d years old." % (name, age))

# .format() method (better than %, but f-strings are usually best)
print("Hello, {}! You are {} years old.".format(name, age))