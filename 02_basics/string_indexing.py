text = "Python Learning for Data Science"

print("String:", text)
print("Length:", len(text), "\n")

# Indexing starts from 0
print("text[0]  →", text[0])     # L
print("text[1]  →", text[1])     # u
print("text[8]  →", text[8])     # space
print("text[10] →", text[10])    # P

# Negative indexing (from the end)
print("text[-1] →", text[-1])    # e (last character)
print("text[-2] →", text[-2])    # c
print("text[-3] →", text[-3])    # n

print("\nFirst character :", text[0])
print("Last character  :", text[-1])

# Trying to access invalid index → error
# print(text[100])              # IndexError

# Small practice:
city = "Delhi"

# Print:
# 1. First letter
print(city[0])
# 2. Last letter
print(city[-1])
# 3. 4th letter (index 3)
print(city[3])
# 4. Second last letter (negative index)
print(city[-2])

print("\nPractice with:", city)