import requests
import os
from twilio.rest import Client


my_OW_id = os.environ.get("API_OW_KEY")
account_sid = os.environ.get("API_TWILIO_SID")
auth_token = os.environ.get("API_TWILIO_TOKEN")

parameters = {
    "units": "metric", # I want temperature in metric units
    "lat": 54.39, # Gdańsk latitude
    "lon": 18.65, # Gdańsk longitude
    "lang": "pl", # in Polish
    "exclude": "current,minutly,daily", # I do not need these parts of forecast
    "appid": my_OW_id
    }

response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=parameters)
# question_data = response.json()
response.raise_for_status()
# print(response.json())
weather_data = response.json()

twelve_codes = []
needs_umbrella = False
for hour in range(12):
    # print(f'Wheather main code: {wheather_data["hourly"][hour]["weather"][0]["id"]}')
    twelve_codes.append(weather_data["hourly"][hour]["weather"][0]["id"])
    if weather_data["hourly"][hour]["weather"][0]["id"] < 700:
        needs_umbrella = True

if needs_umbrella:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Weź parasol.☂️",
                        from_='+16812069655',
                        to='+48609688960'
                    )

    print(message.status)

print(twelve_codes)

