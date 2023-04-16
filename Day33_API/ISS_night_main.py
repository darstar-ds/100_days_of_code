import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 54.352024 # Your latitude
MY_LONG = 18.646639 # Your longitude

my_email = "alle.darstar@gmail.com"
password = "PASSWORD"
is_ISS_visible = False
is_night = True

while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    
    print(f"abs(LAT) = {MY_LAT-iss_latitude}")
    print(f"abs(LONG) = {MY_LONG-iss_longitude}")
    if abs(MY_LAT-iss_latitude)<5 and abs(MY_LONG-iss_longitude)<5:
        is_ISS_visible=True
        print("ISS is above your head")

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour>sunrise and time_now.hour<sunset:
        is_night=False
        print("It is a day right now.")

    if is_night and is_ISS_visible:
        print("It is NIGHT and ISS is visible.")
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs="darstar.misc@gmail.com", 
                msg=f"Subject:ISS alert\n\nGo outside and look in the sky.\nISS is abouve your head."
                )
            print("Email sent.")
    time.sleep(60)
        
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



