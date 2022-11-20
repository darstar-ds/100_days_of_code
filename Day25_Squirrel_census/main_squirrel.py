import pandas as pd
import numpy as np

df = pd.read_csv("./Day25_Squirrel_census/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(df.head(10))
# print(df.columns.values.tolist())
# print(df["Primary Fur Color"])
# print(df["Primary Fur Color"].unique())

squirrel_colors = df["Primary Fur Color"].unique().tolist()
# squirrel_colors = squirrel_colors.tolist()
color_counts = []

for color in squirrel_colors:
    col_count = len(df[df["Primary Fur Color"] == color])
    color_counts.append(col_count)

print(type(squirrel_colors))
print(type(color_counts))

print(squirrel_colors)
print(color_counts)

squirrel_colors.pop(0)
color_counts.pop(0)

print(squirrel_colors)
print(color_counts)

# print(df["Primary Fur Color"].value_counts())

# s_counts = df["Primary Fur Color"].value_counts().to_dict()
# print(s_counts)

#Create a dataframe with squirrel colors
data_dict = {
    "Fur Color": squirrel_colors,
    "Count": color_counts
}

print(data_dict)

s_colors = pd.DataFrame(data_dict)
print(s_colors)
s_colors.to_csv("./Day25_Squirrel_census/s_counts.csv")