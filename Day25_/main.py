# import os

# curr_folder = os.getcwd()
# print(f"Current folder: {curr_folder}")

# lines = []
# with open("./Day25_/weather_data.csv") as forecast:
#     lines = forecast.readlines()
# print(lines)

#########################################################

# import csv

# with open("./Day25_/weather_data.csv") as data_file:
#     ds_data = csv.reader(data_file)
#     temperatures = []
#     for row in ds_data:
#         # print(row)
#         try:
#             temperatures.append(int(row[1]))
#         except:
#             pass
#     print(temperatures)

#########################################################

import pandas as pd
from statistics import mean

df = pd.read_csv("./Day25_/weather_data.csv")
print(df["temp"])

data_dict = df.to_dict()
print(data_dict)

temp_list = df["temp"].to_list()
print(temp_list)

average = mean(temp_list)
print(average)

print(df["temp"].mean())
print(df["temp"].max())

#Get the column
print(df["condition"])
print(df.condition)

#Get the row
print(df[df["day"] == "Monday"])
print(df[df["temp"] == df["temp"].max()])

monday = df[df["day"] == "Monday"]
print(monday.condition)
print((monday.temp)*1.8 + 32)

#Create a dataframe from scratch
data_dict = {
    "student": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

students = pd.DataFrame(data_dict)
print(students)
students.to_csv("./Day25_/students.csv")