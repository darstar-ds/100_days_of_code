import os
import requests
import datetime


my_NUTRITION_id = os.environ.get("API_NUTRITIONIN_ID")
my_NUTRITION_key = os.environ.get("API_NUTRITIONIN_KEY")
sheety_auth_token = os.environ.get("API_SHEETY_AUTH_TOKEN")


GENDER = "MALE"
WEIGHT_KG = "80"
HEIGHT = "6"
AGE = "47"

NLP4EX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_URL = "https://api.sheety.co/e598720cc327978305991b5be8ed94dc/workoutTracking/workouts"

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
    headers = {
        'Authorization': f'Bearer {sheety_auth_token}'
    }
    exercise_name = ex["name"]
    exercise_dur = ex["duration_min"]
    exercise_cal = ex["nf_calories"]
    print(f"Excercise name: {exercise_name}, duration: {exercise_dur}, calories: {exercise_cal}")
    curr_day = datetime.datetime.now()
    ds_day = curr_day.strftime("%d-%m-%Y")
    ds_time = curr_day.strftime("%X")
    print(f"Date: {ds_day}, Time: {ds_time}")
    rows = requests.get(url=SHEET_URL, headers=headers)
    rows.raise_for_status()
    sheet_rows = rows.json()
    print(sheet_rows)
    ds_workout = {
    'workout': {
        'date': str(ds_day),
        'time': str(ds_time),
        'exercise': str(exercise_name),
        'duration': str(exercise_dur),
        'calories': str(exercise_cal)
        }
    }
    print(ds_workout)
    try:
        response = requests.post(url=SHEET_URL, json=ds_workout, headers=headers)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6+
        print(f'Response body: {response.text}')
    except Exception as err:
        print(f'An error occurred: {err}')
    else:
        print('Success!')
