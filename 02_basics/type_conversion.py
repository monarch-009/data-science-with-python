# 1. IMPLICIT Type Conversion (Automatic)
# Python automatically converts one data type to another
# Usually happens during operations (like + * /) to avoid data loss
# Rule: lower precision → higher precision (int → float, etc.)

a = 12          # int
result = a / 2  # division always gives float in Python 3
print("a =", a, "→ type:", type(a))
print("a / 2 =", result, "→ type:", type(result))   # float automatically!
print()

num_int = 10
num_float = 5.75
sum_result = num_int + num_float
print(num_int, "+", num_float, "=", sum_result)
print("Result type:", type(sum_result))     # float (int promoted to float)
print()

# Another common case: int + float → float
print("Implicit rule: Python prefers the more precise type (float > int)")

print("─" * 50)

# 2. EXPLICIT Type Conversion (Manual / Type Casting)
# We (the programmer) decide and use built-in functions
# Very important when input() gives string, or when we need specific type

# Most common conversion functions
print("int()    → to integer")
print("float()  → to float")
print("str()    → to string")
print("bool()   → to boolean (Truthy/Falsy)")
print("list()   → to list")
print("tuple()  → to tuple")
print("set()    → to set")
print("dict()   → usually from pairs (later topic)")
print()

# Examples
age_str = "17"                  # from input() or file usually
age_int = int(age_str)          # explicit conversion
print("String '17' → int:", age_int, type(age_int))

price_str = "499.90"
price_float = float(price_str)
print("String '499.90' → float:", price_float, type(price_float))

num = 100
text = str(num)
print("int 100 → string:", text, type(text))
print("You can now do: 'Your score is ' + text")

print()

# bool() examples (Truthy / Falsy values)
print("bool('hello')  →", bool("hello"))     # True (non-empty string)
print("bool('')        →", bool(""))         # False (empty string)
print("bool(0)         →", bool(0))          # False
print("bool(42)        →", bool(42))         # True
print("bool(None)      →", bool(None))       # False

print("─" * 50)

# Very common real-world example: input() always returns string!
print("Real use-case with input():\n")

# Uncomment and run when ready:
# user_age = input("Enter your age: ")           # always string!
# user_age_int = int(user_age)                   # now it's integer
# print("Next year you'll be:", user_age_int + 1)

# Wrong way (will crash):
# print(user_age + 1)          # TypeError: can't add str + int

print()

# Quick summary table
print("┌─────────────────────┬───────────────────────────────┐")
print("│ Type                │ Common Conversion Function(s) │")
print("├─────────────────────┼───────────────────────────────┤")
print("│ Integer             │ int()                         │")
print("│ Float               │ float()                       │")
print("│ String              │ str()                         │")
print("│ Boolean             │ bool()                        │")
print("│ List                │ list()                        │")
print("│ Tuple               │ tuple()                       │")
print("│ Set                 │ set()                         │")
print("└─────────────────────┴───────────────────────────────┘")

print("\nKey Difference:")
print("• Implicit → Python does it automatically (safe, no data loss)")
print("• Explicit → You do it manually using functions (you control it)")
print()
# Mini Practice Tasks (try to complete them!)

# Task 1: Fix this (uncomment and correct)
score = "85"
bonus = 15
total = int(score) + bonus          # error!
print("Total:", total)

# Task 2: Ask user for two numbers (as strings), convert to int, add them
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
# ... convert and add ...

print(int(num1) + int(num2))

# Task 3: Convert this float to int (what happens to decimal?)
value = 99.99
value_int = int(value)
print("99.99 as int →", value_int)   # hint: it floors / truncates
