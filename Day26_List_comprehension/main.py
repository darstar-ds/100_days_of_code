import random

numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Angela"
new_list = [letter for letter in name]
print(new_list)

doubled_numbers = [n*2 for n in range(1,5)]
print(doubled_numbers)

names_list = ["Alex", "Beth", "Caroline", "Freddie", "Dave", "Eleonor"]
long_names = [name.upper() for name in names_list if len(name)>4]
print(long_names)

students_scores = {student:random.randint(1,100) for student in names_list}
print(students_scores)
passed_students = {student:score for (student,score) in students_scores.items() if students_scores.get(student) > 60}
print(passed_students)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

# Write your code 👇 below:

weather_f = {day:((temp_c*9/5)+32) for (day,temp_c) in weather_c.items()}
print(weather_f)