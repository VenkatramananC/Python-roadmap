# # def welcome(name : str , age : int):
# #   return f"Hello {name} Your age is {age}"


# # print(welcome('Ramana',22.3))

# # name = "Venkat", "Ramanan"
# # split_name = "*".join(name)
# # print(split_name)

# # first = 6.5555
# # second = 5.6677
# # print(first + second)
# # print(round(first + second,2))

# # enclosing scope:
# # name_1 = "rrrrr"
# # def yogi_func():
# #   name_1 = "Ramana"
# #   def ram_func():
# #     print(name_1)
# #   ram_func()


# # yogi_func()

# # def create_character(character_name, strength, intelligence, charisma):
# #     if not isinstance(character_name, str):
# #         return "The character name should be a string"

# #     if len(character_name) > 10:
# #         return "The character name is too long"

# #     if " " in character_name:
# #         return "The character name should not contain spaces"

# #     if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
# #         return "All stats should be integers"

# #     if strength < 1 or intelligence < 1 or charisma < 1:
# #         return "All stats should be no less than 1"

# #     if strength > 4 or intelligence > 4 or charisma > 4:
# #         return "All stats should be no more than 4"

# #     if (strength + intelligence + charisma) != 7:
# #         return "The character should start with 7 points"

# #     max = 10
# #     str_name = "STR " + full_dot * strength + empty_dot * (max - strength)
# #     int_name = "INT " + full_dot * intelligence + \
# #         empty_dot * (max - intelligence)
# #     cha_name = "CHA " + full_dot * charisma + empty_dot * (max - charisma)
# #     return f"{character_name}\n{str_name}\n{int_name}\n{cha_name}"


# # full_dot = '●'
# # empty_dot = '○'
# # print(create_character("Ram", 4, 2, 1))

# # list practice
# # value = ['ram', 'yogi', 'venkat', [23, 44, [33, ['ramanan']]]]
# # del value[3][2][1]
# # print(value)
# # # unpacking values
# # name_1, name_2, name_3, *value = value #asterisk
# # print(name_1)
# # print(value[0])
# # numbers = [1, 3, 4, 5, 5]
# # even = [4,6,8]
# # # numbers.append(even)
# # # print(numbers)
# # numbers.extend(even)
# # print(numbers)
# # numbers.insert(3,4)
# # print(numbers)
# # numbers.remove(4)
# # print(numbers)
# # numbers.pop(3)
# # print(numbers)

# # Tuple:
# # developer = ('Ramana',43,'Java Backend')
# # name = 'VenkatRamanan'
# # print(developer)
# # print(tuple(name))
# # name,*all = developer
# # print(all)
# # sliced_dev = developer[0:1]
# # print(sliced_dev)
# # languages = ('Java', 'Python', 'C++', 'Python', 'C',('Rust','Cloud'))
# # print(sorted(languages, reverse=True))

# # languages_list = ["Python", "Java", "C++", "Rust"]
# # converted_tuple = tuple(languages_list)
# # print(languages_list[0])
# # print(converted_tuple[-1])
# # converted_tuple[0] = "JavaScript"
# # print(converted_tuple)
# # devs = [("Ramana", ["Python", "Java"]),("Yogi", ["C++", "Rust"]),("Venkat", ["Python"])]
# # print(devs[0][0],devs[1][0],devs[2][0])
# # print(devs[1])
# # devs[0][1].insert(2,"Go")
# # print(devs)
# # developer = ("Ramana", 43, "Backend", "Chennai")
# # name, age, *other_infor = developer
# # print(name,age,tuple(other_infor))
# # langs = ("Rust", "Java", "Python", "C", "C++", "Python")
# # print(sorted(langs))
# # print(sorted(langs, reverse=True))
# # print(langs.count("Python"))
# # print(langs.index("Python"))
# def summarize_skills(dev_name, *skills):
#     print(f"Name: {dev_name} ,Total Skills: {len(skills)},Skills: {skills}")
#     print(type(skills))
# summarize_skills("Ramana", "Java", "Python", "C++")

# data = (10, 20, 30, 40, 50, 60)
# first_three = data[0:3]
# last_three = data[3:]
# print(first_three,last_three)

# point = (3, 4)
# x, y = point
# print(f"x = {x}")
# print(f"y = {y}")

# t1 = (1, 2)
# t2 = (3, 4)
# t1,t2 = t2,t1
# print(t1,t2)

# nums = (1, 2, 3, 4, 5, 6)
# for num in nums:
#     if num % 2 == 0:
#         print(num, end=" ")

# lst = [10, 20, 30]
# print(list(tuple(lst)))


# nested = (1, (2, 3), (4, (5, 6)))
# fifth = nested[2][1][0]
# print(fifth)

# for loop:
# programming_languages = ['Java', 'Python', 'Javascript']
# for language in programming_languages:
#   print(language)
#   if language == programming_languages[0]:
#     res = "".join(programming_languages[1:len(programming_languages)])
#     print(res)
#     break
# nested for loop
# categories = ['Fruits', 'Vegetables']
# food = ['Apple', 'Orange', 'Bannana', 'Carrot', 'Tomato']
# for category in categories:
#     for fruit in food:
#         print(category, fruit)

# for loop Exercise:
# for i in range(1,21):
#   print(i,end=" ")
# print()
# for i in range(2,101):
#   if i % 2 == 0:
#     print(i,end=" ")
# nums = [3, 7, 2, 9, 4]
# max = 0
# for i in nums:
#     print(i, end=" ")
#     if i > max:
#         max = i
# print(max)
# print(max(nums))
# langs = ["Python", "Java", "C++", "Rusts"]
# for i in langs:
#     if len(i) > 4:
#         print(i)
# num = int(input("Enter the value to print: "))
# for i in range(1, num+1):
#     for j in range(0, i):
#         print("*",end="")
#     print()
# num = 5
# for i in range(1,num+1):
#   print(i*i)
# text = "Ramana"
# for i in text:
#   print(text.index(i),i)
# total = 0
# for i in text:
#   if i in 'aeiou':
#     total+=1
# print(total)
# def filter_long_words(words, min_len):
#     new_list = []
#     for i in words:
#         if len(i) >= min_len:
#             new_list.append(i)
#     return new_list


# print(filter_long_words(["java", "python", "go", "rust"], 4))


# #While loop:
# secret_number = 3
# guess = 0
# while guess != secret_number:
#   guess = int(input("Guess the secret no (1-5): "))
#   if guess != secret_number:
#     print("Wrong found, Don't give up try again")
# print("You got it ",secret_number)


# Enumerate:
# languages = ['Spanish', 'English', 'Tamil']
# for language in enumerate(languages,1):
#   print(f'{language}')

# Zip():
# ids = [1,2,3]
# for name, id in zip(languages,ids):
#   print(id)
#   print(name)

# List comprehension:
# numbers = int(input("Enter to find odd or even: "))
# even_numbers = [(numbers,"Its a Even Number") if numbers % 2 == 0 else (numbers,"Its a Odd NUmber")]
# print(str(even_numbers))
# exercise in list comprehension:
# nums = [1, 2, 3, 4, 5]
# squares = [nums**3 for nums in nums]
# print(squares)
# languages = ['Python','Java','C','Rust']
# len_languages = [len(language) for language in languages]
# print(len_languages)
# nums = list(range(1, 21))
# even_numbers = [num for num in nums if num % 2 == 0]
# print(even_numbers)
# divisible_by_3 = [num for num in nums if num % 3 == 0]
# print(divisible_by_3)
# words = ["apple", "hi", "banana", "go", "orange"]
# words_with_greater_than_4 = [word for word in words if len(word) >= 4]
# print(words_with_greater_than_4)
# marks = [35, 80, 60, 90]
# highest_marks = [(mark, 'Pass') if mark >= 40 else (mark, 'Fail') for mark in marks]
# print(highest_marks)
# filter() function


# def is_even(x):
#     return x % 2 == 0


# num = [1, 2, 3, 4, 5, 6]
# print(list(filter(is_even, num)))
# print(list(filter(lambda x: x % 2 == 0, num)))
# Exercise
# def num_greater_50(x):
#   return x > 50


# def less_than_1(x):
#   return x < 0


# num = [20,34,65,45,78,58,-2,-34,-1]
# greater_50 = filter(num_greater_50,num)
# negative_numbers = filter(less_than_1, num)
# print(list(greater_50))
# print(list(negative_numbers))
# words = ["hi", "python", "is", "", "awesome", "go", ""]
# greater_words = filter(lambda x: len(x) >= 4, words)
# removed_empty_string = filter(None,words)
# print(list(greater_words))
# print(list(removed_empty_string))
# def vowels(x):
#     return list(filter(lambda x: x in 'AEIOU',x))
# names = ["Akash", "Meena", "Om", "sha", "Rohan"]
# contains_vowels = filter(vowels, names)
# print(list(contains_vowels))
# nums = list(range(1, 31))
# div_by_both_2_3 = filter(lambda x: x % 2 == 0 and x % 3 == 0,nums)
# print(list(div_by_both_2_3))
# text = "List Comprehension and Filter"
# vowels_words = filter(lambda x: x in 'AEIOUaeiou',text)
# print(list(vowels_words))
# numbers = [1,2,3,4]
# squ = [2,3,4,5]
# sum = filter(lambda n,r: n + r ,numbers,squ)
# print(list(sum))

# string = """The value of the item
# And the another one is"""
# splicted = string.split("\n")
# print(splicted)

# def numm(n):
#     value = ''
#     if not isinstance(n, int) and n < 1:
#         return "Argument must be an integer greater than 0."
#     for n in range(1, n+1):
#         value += str(n) + ' '
#     return value.strip()
# outt = numm()
# print(str(outt))

# number = [20,30,40]
# number.append(10)
# number.append(20)
# number.append(30)
# print(*number)
# number = int(input())
# total = sum(number)
# print(total)
# def is_name():
#     while True:
#         try:
#             name = input("Enter your name: ")
#             if isinstance(name, str):
#                 return name
#         except:
#             print("Enter name only")


# print(is_name)

# name = "Pen"
# price = 1.5
# print(f"{name:<10}{price:.2f}")

# day 1 exercises:
# 1 name , age , height = input("Enter Your name , age, height : ").split()
# age = int(age)
# try:
#   height = float(height)
#   print(f"{name} is {age} years old, {height} ft tall")
# except:
#   print("You entered wrong height")
numbers = input("3 nums: ").split()
numbers = list(map(int,numbers))
print(sum(numbers))
# weight, height = input("Enter your weight, height : ").split()
# try:
#     weight = float(weight)
#     height = float(height)
#     bmi = weight/(height**2)
#     if 18.5 <= bmi <= 24.9:
#         print("Normal")
#     else:
#         print("Adjust")
# except:
#     print("Entered wrong input weight or height")


# /3 while True:
#   name = input("Enter your name: ").strip()
#   if name.replace(" ","").isalpha():
#     print("Welcome")
#     break
a = 10
b = 3
print(f"{a // b} {a % b} {a ** b}")
