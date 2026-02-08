# Basic math operations in Python (+ - * / // % **)
print("Arithmetic Operators ===\n")

a = 15
b = 4

print("a =", a, "   b =", b, "\n")

# Addition
print("a + b  =", a + b)      # 19

# Subtraction
print("a - b  =", a - b)      # 11

# Multiplication
print("a * b  =", a * b)      # 60

# Division (always gives float in Python 3)
print("a / b  =", a / b)      # 3.75

# Floor division (integer division - removes decimal part)
print("a // b =", a // b)     # 3

# Modulus / Remainder
print("a % b  =", a % b)      # 3   (because 15 = 3*4 + 3)

# Exponent / Power
print("a ** b =", a ** b)     # 15⁴ = 50625
print("2 ** 10 =", 2 ** 10)   # 1024 (very common!)

print("\nQuick real-life examples:")
distance_km = 120
fuel_used_liters = 8.5
km_per_liter = distance_km / fuel_used_liters
print("Mileage =", round(km_per_liter, 2), "km/l")

# Mini tasks:
# 1. Calculate area of rectangle (length × width)
# 2. Calculate simple interest: (principal × rate × time) / 100
# 3. Find how many full chocolates you can buy with 200 rupees if each costs 17 rupees