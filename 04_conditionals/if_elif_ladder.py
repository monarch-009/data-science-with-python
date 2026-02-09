# Handling multiple conditions in order (if → elif → elif → ... → else)

print("=== if - elif - else Ladder ===\n")

marks = 78

if marks >= 90:
    print("Grade: A+")
    print("Outstanding!")
elif marks >= 80:
    print("Grade: A")
    print("Very good")
elif marks >= 70:
    print("Grade: B")
    print("Good")
elif marks >= 60:
    print("Grade: C")
    print("Average")
elif marks >= 40:
    print("Grade: D")
    print("Just passed")
else:
    print("Grade: F")
    print("Failed - try again")

# ----------------------

print("\nReal-life example: traffic light simulation\n")

light = "yellow"  # try changing to "red", "green", "yellow"

if light == "green":
    print("Go!")
elif light == "yellow":
    print("Slow down / prepare to stop")
elif light == "red":
    print("STOP!")
else:
    print("Invalid light color")

# ----------------------

print("\nOrder matters! First true condition wins → others are skipped")

score = 85
if score > 80:
    print("High score!")
elif score > 50:
    print("Okay score")
elif score > 30:
    print("Low score")

# Mini tasks:
# 1. Create grade system: >90 → Excellent, >75 → Very Good, >60 → Good, else → Needs Improvement
# 2. Ask user for age → categorize: <13 child, <20 teenager, <60 adult, else senior
# 3. Write condition for discount: >5000 → 20%, >2000 → 10%, >500 → 5%, else 0%