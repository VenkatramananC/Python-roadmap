name = input("Enter your name: ")
if name:
    print("Valid name")
else:
    print("Name required")

num = int(input("Enter a number: "))
if num == 0:
    print("Zero detected")
print(num)

name = input("Enter username: ")
password = input("Enter password: ")
if name == "admin" and len(password) >= 8:
  print("Accepted")
else:
  print("Not")

age = int(input("Enter your age: "))
student_id = input("enter True if you are student else False : ")
student_id = student_id.capitalize()
if age < 10 or student_id:
  print("Free")
else:
  print("Adult")

price = float(input("Enter how much did you purchase: "))
premium_member = input("Enter yes if you are pm else empty: ")
if price > 500 or not premium_member:
  print((price * (20/100)) + price)
else:
  print("No")

speed_camera = 101
if speed_camera <= 60:
  print("Safe")
elif 60 < speed_camera <= 80:
  print("Warning")
elif 80 < speed_camera <= 100:
  print("Fine 500")
else:
  print("license suspended")

bmi = float(input("Enter your BMI: "))
if bmi <= 18.5:
  print("Underweight")
elif 18.5 < bmi <= 24.9:
  print("Normal")
elif 25 <= bmi <=29.9: 
  print("Overweight")
else:
  print("Obese")

party_size = int(input("Enter size party: "))
has_reservation = bool(input("Enter yes if you are reserved else Empty: "))
if party_size <= 4 or has_reservation:
  print("Table")
else:
  print("Waitlist")

mail = input("Enter your mail: ")
if "@" in mail and mail.endswith(".com") or mail.endswith(".in") and len(mail) >= 5:
  print("Valid")
else:
  print("Not valid")