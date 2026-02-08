age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
    print("You can vote.")
    print("You can get a driving license (in most places).")
else:
    print("You are underage")

print("\nThis line always runs (outside the if block)")

# ----------------------

temperature = 28

if temperature > 30:
    print("It's very hot today!")

if temperature < 15:
    print("It's quite cold.")

print("Current temperature:", temperature)

# ----------------------

# Most common real use: checking conditions from input
# marks = int(input("Enter your marks: "))
# if marks >= 40:
#     print("Congratulations! You passed.")

print("\nImportant points about if:")
print("• No parentheses needed around condition")
print("• Condition must end with :")
print("• Indentation (usually 4 spaces) defines the block")
print("• If condition is False → block is skipped completely")

# Mini tasks:
# 1. Write if that prints "Positive" if a number > 0
num = 55
if num > 0:
    print("Positive")
# 2. Write if that prints "Even" if number % 2 == 0

# 3. Ask user for a number and print "Big number!" if it's > 100