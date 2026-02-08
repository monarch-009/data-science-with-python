# Compare values → return True or False (boolean)

print("Comparison Operators\n")

a = 20
b = 15
c = 20

print("a =", a, "  b =", b, "  c =", c, "\n")

print("a == b  →", a == b)     # Equal to?          False
print("a == c  →", a == c)     #                     True
print("a != b  →", a != b)     # Not equal to?      True
print("a > b   →", a > b)      # Greater than?      True
print("a < b   →", a < b)      # Less than?         False
print("a >= c  →", a >= c)     # Greater or equal?  True
print("b <= c  →", b <= c)     # Less or equal?     True

print("\nWith strings (compares alphabetically/lexicographically)")
print("'apple' < 'banana' →", "apple" < "banana")     # True
print("'Python' == 'python' →", "Python" == "python") # False (case-sensitive)
print("'cat' > 'car' →", "cat" > "car")               # True ('t' > 'r')

print("\nCommon mistake:")
print("5 == '5'  →", 5 == "5")      # False (int vs str)
print("5 == int('5') →", 5 == int("5"))  # True

# Mini task:
age = 17
height = 165.5

# Print whether:
# 1. age is greater than or equal to 18
print(age>=18)
# 2. height is between 150 and 180 (use two comparisons)
print(height >= 150 and height <= 180)
# 3. age == 17
print(age == 17)