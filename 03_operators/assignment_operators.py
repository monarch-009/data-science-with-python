print("Assignment Operators ===\n")

score = 50
print("Initial score:", score)

# Basic assignment
score = 75
print("After score = 75 →", score)

# +=   (add and assign)
score += 10          # same as: score = score + 10
print("score += 10 →", score)   # 85

# -=
score -= 25
print("score -= 25 →", score)   # 60

# *=
score *= 2
print("score *= 2  →", score)   # 120

# /=
score /= 3
print("score /= 3  →", score)   # 40.0

# //=
score //= 4
print("score //= 4 →", score)   # 10.0

# %=
score %= 7
print("score %= 7  →", score)   # 3.0

# **=
score **= 3
print("score **= 3 →", score)   # 27.0

print("\nMost commonly used: += and -= ")
print("Very useful in loops and counters")
