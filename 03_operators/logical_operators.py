# Combine conditions: and, or, not

print("Logical Operators \n")

age = 17
has_voter_id = False
has_aadhar = True

print("age =", age)
print("has_voter_id =", has_voter_id)
print("has_aadhar =", has_aadhar, "\n")

# and → both must be True
print("Can vote? (age >= 18 and has_voter_id) →",
      age >= 18 and has_voter_id)                    # False

# or → at least one must be True
print("Can enter club? (age >= 18 or has_aadhar) →",
      age >= 18 or has_aadhar)                       # True

# not → reverses the boolean
print("not has_voter_id →", not has_voter_id)        # True
print("not (age > 20) →", not (age > 20))            # True

print("\nCombining them:")
print("Teenager with ID: (13 <= age <= 19) and has_aadhar →",
      (13 <= age <= 19) and has_aadhar)              # True

print("\nShort-circuit evaluation (Python stops if it already knows result)")
print("True or anything → always True")
print("False and anything → always False")

# Task:
marks = 82
attendance = 78

# Check if student passes if:
# marks >= 75 AND attendance >= 75
print("Pass?", marks >= 75 and attendance >= 75)

# Or passes with grace if marks >= 90 OR attendance >= 90
print("Grace pass?", marks >= 90 or attendance >= 90)