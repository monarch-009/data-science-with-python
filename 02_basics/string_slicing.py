phrase = "Python is awesome and fun"

print("Full string:", phrase)
print("Length   :", len(phrase), "\n")

# Basic slicing [start:end:step] → end is NOT included
print("phrase[0:6]   →", phrase[0:6:2])     # Pto
print("phrase[7:9]   →", phrase[7:9])     # is
print("phrase[10:17] →", phrase[10:17])   # awesome

# From start to some position
print("phrase[:6]    →", phrase[:6])      # Python (start=0)

# From some position to end
print("phrase[10:]   →", phrase[10:])     # awesome and fun

# Every second character [start:end:step]
print("phrase[::2]   →", phrase[::2])     # Pto saeoe n u
print("phrase[1::2]  →", phrase[1::2])    # yhn i wseadfn

# Reverse the string
print("phrase[::-1]  →", phrase[::-1])    # nuf dna emosewa si nohtyP

# Some common useful slices
print("\nFirst 5 chars  :", phrase[:5])
print("Last 5 chars   :", phrase[-5:])
print("Without first & last:", phrase[1:-1])


# Task:
word = "Programming"

# Try to get these using slicing:
# 1. "Pro"
print(word[0:3])
# 2. "ming"
print(word[7:])
# 3. "gram"
print(word[3:7])
# 4. reverse the word
print(word[::-1])