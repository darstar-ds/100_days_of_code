import os
import requests
import json


my_NUTRITION_id = os.environ.get("API_NUTRITIONIN_ID")
my_NUTRITION_key = os.environ.get("API_NUTRITIONIN_KEY")


GENDER = "MALE"
WEIGHT_KG = "80"
HEIGHT = "6"
AGE = "47"

NLP4EX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_input = input("Tell which exercise you did today?: ")

header = {
"x-app-id": my_NUTRITION_id,
"x-app-key": my_NUTRITION_key,
}

parameters = {
"query": exercise_input,
"gender": GENDER,
"weight_kg": WEIGHT_KG,
"height_cm": HEIGHT,
"age": AGE,
}

# print(f"key: {my_NUTRITION_id}")
# print(f"id: {my_NUTRITION_key}")
response = requests.post(url=NLP4EX_ENDPOINT, json=parameters, headers=header)
response.raise_for_status()
result = response.json()
print(result)

for ex in result["exercises"]:
    exercise_name = ex["name"]
    exercise_dur = ex["duration_min"]
    exercise_cal = ex["nf_calories"]
    print(f"Excercise name: {exercise_name}, duration: {exercise_dur}, calories: {exercise_cal}")
