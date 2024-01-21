import os
from twilio.rest import Client

account_sid = os.environ.get("API_TWILIO_SID")
auth_token = os.environ.get("API_TWILIO_TOKEN")
print(f"{account_sid} - {auth_token}")


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_alert(self, 
                   price, 
                   depart_city_name, 
                   depart_iata_code, 
                   dest_city_name, 
                   dest_iata_code,
                   depart_date,
                   arrival_date
                    ):

        client = Client(account_sid, auth_token)
        promo_news = f"Low price alert! Only {price} GBP to fly " + \
                        f"from {depart_city_name}-{depart_iata_code} " + \
                        f"to {dest_city_name}-{dest_iata_code} " + \
                        f"from {depart_date} to {arrival_date}"
        message = client.messages \
                        .create(
                            body= promo_news,
                            from_='+16508439966',
                            to='+48609688960'
                        )

        print(message.status)
