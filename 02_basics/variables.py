# === What is a variable? ===
# A variable is like a labeled box where you can store a value
# You give the box a name and put something inside it

# --- Basic examples ---
age = 17                  # integer (whole number)
height = 5.6              # float (number with decimal)
name = "Aditya"           # string (text) — use quotes
is_learning = True        # boolean (True or False)

# You can check what’s inside any variable using print()
print("My name is:", name)
print("I am", age, "years old")
print("My height is", height, "feet")
print("Learning Python?:", is_learning)

print("─" * 40)

# === You can change the value later (variables are mutable) 
age = 18
print("Next year I will be:", age)

print("─" * 40)

# === Python is dynamically typed (you don't need to say the type)
points = 120       # was integer
points = "one twenty"   # now it's a string — no error!
print("points =", points)

print("─" * 40)

# === Multiple assignment (cool trick) 
x, y, z = 10, 20, "hello"
print(x, y, z)

# Same value to many variables
a = b = c = 100
print(a, b, c)

print("─" * 40)

# === Most common built-in types (very important) 
integer = 42
floating = 3.14
text = "Python is fun"
boolean = True
nothing = None          # special value meaning "nothing here"

print(type(integer))    # <class 'int'>
print(type(floating))   # <class 'float'>
print(type(text))       # <class 'str'>
print(type(boolean))    # <class 'bool'>
print(type(nothing))    # <class 'NoneType'>
