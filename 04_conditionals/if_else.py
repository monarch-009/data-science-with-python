# if + else → do one thing or the other

print("if-else Statement\n")

age = 16

if age >= 18:
    print("You can vote.")
    print("Adult section")
else:
    print("You are still a minor.")
    print("Come back after", 18 - age, "years.")

# ----------------------

marks = 72

if marks >= 40:
    print("Result: PASS")
    print("Well done!")
else:
    print("Result: FAIL")
    print("Better luck next time.")

# ----------------------

# Common pattern: even / odd
number = 45

if number % 2 == 0:
    print(number, "is EVEN")
else:
    print(number, "is ODD")

# ----------------------


# Mini practice tasks:
# 1. Ask user for a number → print "Positive", "Negative" or "Zero"
# 2. Ask for temperature → if >= 25 print "Summer vibes", else "Cool weather"
# 3. Check password: if input == "python123" print "Access granted", else "Wrong password"