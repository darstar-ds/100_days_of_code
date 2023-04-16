import requests
from datetime import datetime

MY_LAT = 54.352024
MY_LNG = 18.646639

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
# print(sunrise.split("T")[1].split(":")[0])

time_now = datetime.now()
print(time_now.hour)