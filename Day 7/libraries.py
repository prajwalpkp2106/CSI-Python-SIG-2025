# -------------------------------
# Python Libraries Example
# -------------------------------

# # ====== 1. MATH LIBRARY ======
# import math

# print("=== MATH LIBRARY EXAMPLES ===")

# x = 16
# y = 3

# print(f"Square root of {x}:", math.sqrt(x))          # √16 = 4.0
# print(f"{x} raised to the power {y}:", math.pow(x, y))  # 16³ = 4096.0
# print(pow(2,3))
# print("Value of PI:", math.pi)
# print(f"Floor value of 7.8:", math.floor(7.8))      # rounds down
# print(math.floor(2.1))

# print()  

# # ====== 2. RANDOM LIBRARY ======
# import random

# print("=== RANDOM LIBRARY EXAMPLES ===")

# a, b = 1, 10
# sequence = ['apple', 'banana', 'cherry', 'mango',12]

# print(f"Random integer between {a} and {b}:", random.randint(a, b))
# print("Random choice from list:", random.choice(sequence))

# print()

# ====== 3. DATETIME LIBRARY ======
import datetime

print("=== DATETIME LIBRARY EXAMPLES ===")

# Get current date and time
dt = datetime.datetime.now()
print("Current Date & Time:", dt)

# Format the date and time
formatted = dt.strftime("%m-%d-%Y %H:%M:%S")
print("Formatted Date & Time:", formatted)

# Example: show individual components
print("Year:", dt.year)
print("Month:", dt.month)
print("Day:", dt.day)
print("Hour:", dt.hour)
print("Minute:", dt.minute)
print("Second:", dt.second)
