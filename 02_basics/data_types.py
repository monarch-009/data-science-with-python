# 1. int → whole numbers (positive, negative, zero)
age = 17
temperature_today = -3
very_big_number = 9876543210
print("int examples:", age, temperature_today, very_big_number)
print("Type of age:", type(age))           # <class 'int'>
print()

# 2. float → numbers with decimal point
height = 5.7
pi = 3.14159
weight = 68.25
print("float examples:", height, pi, weight)
print("Type of pi:", type(pi))             # <class 'float'>
print()

# 3. str → strings (text) - use single or double quotes
name = "Aditya"
city = 'Ludhiana'
emoji = "Python 🐍 is fun"
long_text = """This is a 
multi-line string"""
print("str examples:", name, city, emoji)
print("First letter of name:", name[0])     # A
print("Type of name:", type(name))          # <class 'str'>
print()

# 4. bool → boolean values: only two possible values
is_student = True
has_finished_homework = False
is_raining = False
print("bool examples:", is_student, has_finished_homework)
print("Type of is_student:", type(is_student))   # <class 'bool'>
print("5 > 10 →", 5 > 10)                        # False
print("100 == 100 →", 100 == 100)                # True
print()

# 5. NoneType → represents the absence of a value (like null in other languages)
nothing = None
result = None
print("None example:", nothing)
print("Type of nothing:", type(nothing))     # <class 'NoneType'>
print()

# ────────────────────────────────────────────────
# Quick summary table (just printed)
# ────────────────────────────────────────────────
print("┌─────────────┬───────────────────────┬──────────────┐")
print("│ Type        │ Example               │ Python name  │")
print("├─────────────┼───────────────────────┼──────────────┤")
print("│ Whole num   │ 17, -5, 0             │ int          │")
print("│ Decimal     │ 3.14, -0.001, 5.0     │ float        │")
print("│ Text        │ \"Hello\", 'Python'     │ str          │")
print("│ True/False  │ True, False           │ bool         │")
print("│ No value    │ None                  │ NoneType     │")
print("└─────────────┴───────────────────────┴──────────────┘\n")

# ────────────────────────────────────────────────
# Very useful: type() function tells you the type
# ────────────────────────────────────────────────
print("type(42)     →", type(42))
print("type(3.14)   →", type(3.14))
print("type(\"hi\")  →", type("hi"))
print("type(True)   →", type(True))
print("type(None)   →", type(None))
print()
