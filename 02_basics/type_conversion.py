# How should you name variables, functions, files in Python?

# Python has strong community conventions (mostly from PEP 8)


# 1. snake_case → most common for variables and functions
user_name = "Aditya"
total_marks = 485
is_adult = True
calculate_average = 89.5

# 2. lowercase with underscore (same as snake_case)
max_attempts = 5
game_score = 0

# 3. CAPITAL_SNAKE_CASE → constants (values you never plan to change)
MAX_PLAYERS = 4
PI = 3.14159
DEFAULT_TIMEOUT = 30

# 4. CamelCase or PascalCase → usually for class names (we'll learn later)
class StudentRecord:
    pass


# camelCase (JavaScript style - not common in Python)
userName = "Aditya"          # ← don't do this

# PascalCase for variables (looks like class name)
UserAge = 17                 # ← confusing

# very short non-descriptive names (except for very small loops)
x = 10                       # okay in short loops
abcdefgh = "something"       # bad — what is this??

# starting with numbers
# 1st_place = "gold"           # SyntaxError!

# using Python reserved words
# class = "python"             # SyntaxError!
# print = 123                  # dangerous - breaks built-in print()



