"""
DAY 1-2 PYTHON MASTERY ✅
Completed: Dec 24, 2025
Skills: Variables, Input, Types, Error Handling, Loops
Confidence: 95%
Next: Day 3 - if/else + Logical Operators
"""

# Task 1: Type Conversion + Error Handling
print("=== TASK 1: Type Conversion ===")
name, age_str, height_str = input("Name, age, height: ").split()
age = int(age_str)
try:
    height = float(height_str)
    print(f"{name} is {age} years old, {height} ft tall")
except ValueError:
    print("Wrong height format!")

print("\n=== TASK 2: Multi-Input Sum ===")
numbers = input("3 nums: ").split()
numbers = list(map(int, numbers))
print(f"Sum: {sum(numbers)}")

print("\n=== TASK 3: BMI Calculator ===")
weight, height = input("Weight(kg), height(m): ").split()
try:
    weight = float(weight)
    height = float(height)
    bmi = weight / (height ** 2)
    if 18.5 <= bmi <= 24.9:
        print("Normal")
    else:
        print("Adjust")
except ValueError:
    print("Wrong input!")

print("\n=== TASK 4: Valid Name Loop ===")
while True:
    name = input("Name (letters): ").strip()
    if name.replace(" ", "").isalpha():
        print(f"Welcome {name}!")
        break
    print("Letters only!")

print("\n=== TASK 5: Arithmetic Chain ===")
a, b = 10, 3
print(f"{a//b} {a%b} {a**b}")  # 3 1 1000

print("\n🎉 DAY 1-2: 100% MASTERED!")
