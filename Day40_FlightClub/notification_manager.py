import os
import smtplib
from pprint import pprint
from data_manager import DataManager
from twilio.rest import Client

account_sid = os.environ.get("API_TWILIO_SID")
auth_token = os.environ.get("API_TWILIO_TOKEN")
print(f"{account_sid} - {auth_token}")

my_email = "alle.darstar@gmail.com"
password = os.environ.get("ALLE_DARSTAR_GMAIL")

sheety_auth_token = os.environ.get("API_SHEETY_AUTH_TOKEN")
sheety_users_sheet_url = "https://api.sheety.co/e598720cc327978305991b5be8ed94dc/dsFlightDeals/users"

obj_users = DataManager(sheety_auth_token, sheety_users_sheet_url)
sheet_data_users = obj_users.get_users()
pprint(sheet_data_users)

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_alert(self, 
                   price,
                   via_city, 
                   depart_city_name, 
                   depart_iata_code, 
                   dest_city_name, 
                   dest_iata_code,
                   depart_date,
                   arrival_date
                    ):

        client = Client(account_sid, auth_token)
        promo_news_0stop = f"Low price alert! Only {price} GBP to fly " + \
                        f"from {depart_city_name}-{depart_iata_code} " + \
                        f"to {dest_city_name}-{dest_iata_code} " + \
                        f"from {depart_date} to {arrival_date}"
        promo_news_1stop = f"Low price alert! Only {price} GBP to fly " + \
                        f"from {depart_city_name}-{depart_iata_code} " + \
                        f"to {dest_city_name}-{dest_iata_code} " + \
                        f"from {depart_date} to {arrival_date}\n" + \
                        f"Flight has 1 stop over, via {via_city}."
        if via_city == "":
            promo_news = promo_news_0stop
        else:
            promo_news = promo_news_1stop

        message = client.messages.create(
                            body= promo_news,
                            from_='+16508439966',
                            to='+48609688960'
                            )

        print(message.status)

    def send_emails(self, 
                   price,
                   via_city, 
                   depart_city_name, 
                   depart_iata_code, 
                   dest_city_name, 
                   dest_iata_code,
                   depart_date,
                   arrival_date
                    ):

        promo_news_0stop = f"Low price alert! Only {price} GBP to fly " + \
                        f"from {depart_city_name}-{depart_iata_code} " + \
                        f"to {dest_city_name}-{dest_iata_code} " + \
                        f"from {depart_date} to {arrival_date}"
        promo_news_1stop = f"Low price alert! Only {price} GBP to fly " + \
                        f"from {depart_city_name}-{depart_iata_code} " + \
                        f"to {dest_city_name}-{dest_iata_code} " + \
                        f"from {depart_date} to {arrival_date}\n" + \
                        f"Flight has 1 stop over, via {via_city}."
        if via_city == "":
            promo_news = promo_news_0stop
        else:
            promo_news = promo_news_1stop

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for entry in sheet_data_users['users']:
                connection.sendmail(
                        from_addr = my_email, 
                        to_addrs = entry['email'], 
                        msg = f"Subject:Flight deal\n\n{promo_news}."
                        )