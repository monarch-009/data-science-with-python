# Problem 1: Calculate final price after discount
original_price = 1200
discount_percent = 15

discount_amount = original_price * discount_percent / 100
final_price = original_price - discount_amount

print(f"Original: ₹{original_price}")
print(f"Discount: {discount_percent}% → ₹{discount_amount}")
print(f"Final price: ₹{final_price}\n")

# Problem 2: Check if number is even or odd
num = 28
is_even = num % 2 == 0
print(f"{num} is even? {is_even}")

# Problem 3: Temperature conversion °C → °F
celsius = 38
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F\n")

# Problem 4: Login condition
username = "aditya"
password = "python123"
input_user = "aditya"
input_pass = "python123"

correct_login = (username == input_user) and (password == input_pass)
print("Login successful?", correct_login)

# Problem 5: Simple eligibility checker
age = 19
has_license = True
has_vehicle = False

can_ride_bike = age >= 18 and has_license
can_buy_car = age >= 21 or (age >= 18 and has_license and has_vehicle)

print("Can ride bike?", can_ride_bike)
print("Can buy car? ", can_buy_car)


# Ideas:
# 1. BMI calculator (weight_kg / height_m ** 2)
weight = 69
height = 2
print("BMI: ",weight/height ** 2)

# 2. Check if a year is leap year (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
year = int(input("Enter year: "))
print(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
# 3. Calculate total with tax (price * 1.18)
price = 100
print(price*1.18)