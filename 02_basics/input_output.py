# Basic input
name = input("What is your name? ")
print("Hello,", name)

# Input for numbers (remember: input() returns string)
age = int(input("How old are you? "))
# age = int(age_str)  # convert to integer
print("Next year you will be", age + 1)

# Better way (combine in one line)
height = float(input("Enter your height in feet: "))
print("Your height is", height, "feet")

print()

# Nicer output formatting - f-strings (Python 3.6+)
city = "Patna"
learning_days = 15

print(f"Hi! I am from {city} and learning Python for {learning_days} days.")
print(f"{name} is {age} years old.")

# Older ways (still work)
print("Hi! I am from %s." % city)
print("Hi! I am from {} and learning for {} days.".format(city, learning_days))

print()

# Multiple inputs in one line (simple way)
x, y = input("Enter two numbers separated by space: ").split()
x = int(x)
y = int(y)
print("Sum:", x + y)

# Mini project idea:
# Ask user:
# 1. name
name = input("Enter name: ")
print("Name: ", name)
# 2. age
age = int(input("Enter your age: "))
print("Age: ",age)
# 3. favorite programming language
language = input("Favoutite Lannguage: ")
print("Fav Language: ",language)
# Then print a nice summary using f-string
print(f"Name : {name} Age : {age} language : {language}")