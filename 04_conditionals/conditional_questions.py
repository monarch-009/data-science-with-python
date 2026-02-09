# conditional_questions.py
# Practice problems using if / elif / else

print("=== Conditional Practice Questions ===\n")

# Question 1
print("Q1: Even or Odd + multiple of 5?")
num = 35

if num % 2 == 0:
    print("Even")
    if num % 5 == 0:
        print("→ also multiple of 5")
else:
    print("Odd")
    if num % 5 == 0:
        print("→ but multiple of 5")

# Question 2
print("\nQ2: Largest among three numbers")
a, b, c = 45, 78, 23

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# Question 3
print("\nQ3: Triangle validity")
side1, side2, side3 = 5, 6, 12

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("Valid triangle")
else:
    print("Not a valid triangle")

# Question 4
print("\nQ4: Simple calculator choice")
print("Choose operation:")
print("1 → Add")
print("2 → Subtract")
print("3 → Multiply")
print("4 → Divide")

# choice = int(input("Enter choice (1-4): "))
# num1 = float(input("Number 1: "))
# num2 = float(input("Number 2: "))

# if choice == 1:
#     print("Result:", num1 + num2)
# elif choice == 2:
#     print("Result:", num1 - num2)
# elif choice == 3:
#     print("Result:", num1 * num2)
# elif choice == 4:
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Cannot divide by zero!")
# else:
#     print("Invalid choice")

print("\nNow try to solve these on your own:")
print("1. Check if year is leap year")
print("   (div by 4 and (not div by 100 or div by 400))")
print("2. Ask user for 3 subject marks → print pass/fail + percentage + grade")
print("3. Rock-Paper-Scissors logic (you vs computer)")

print("\nMaster these → you're ready for loops!")