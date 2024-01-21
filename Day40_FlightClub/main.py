#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import timedelta, datetime

sheety_auth_token = os.environ.get("API_SHEETY_AUTH_TOKEN")
sheety_sheet_url = "https://api.sheety.co/e598720cc327978305991b5be8ed94dc/dsFlightDeals/prices"

obj = DataManager(sheety_auth_token, sheety_sheet_url)
sheet_data = obj.get_prices()
pprint(sheet_data)

is_iataCode_empty = True
for entry in sheet_data['prices']:
    # Access the 'iataCode' for each city.
    iata_code = entry['iataCode']
    if iata_code != "":
        print(f"City: {entry['city']}, IATA Code: {iata_code}")
        is_iataCode_empty = False
print(is_iataCode_empty)

# for entry in sheet_data['prices']:
#     city_name = entry['city']
#     row_id = entry['id']
#     getting_code = FlightSearch()
#     ds_iataCode = getting_code.get_iataCode(city_name)
#     inserting_code = DataManager(sheety_auth_token, sheety_sheet_url)
#     insert_code = inserting_code.insert_iataCode(ds_iataCode, row_id)

for entry in sheet_data['prices']:
    dest_city_IATA_code = entry['iataCode']
    dest_min_price = entry['lowestPrice']
    min_start_date = datetime.now() + timedelta(days = 1)
    # print(type(min_start_date))
    min_start_date_DD = min_start_date.day
    min_start_date_MM = min_start_date.month
    min_start_date_YYYY = min_start_date.year
    # print(f"DD={min_start_date_DD}, MM={min_start_date_MM}, YYYY={min_start_date_YYYY}")
    # min_start_date_param = min_start_date.strftime("%x")
    min_start_date_param = f"{min_start_date_DD}/{min_start_date_MM}/{min_start_date_YYYY}"
    max_start_date = datetime.now() + timedelta(days = 180)
    max_start_date_DD = max_start_date.day
    max_start_date_MM = max_start_date.month
    max_start_date_YYYY = max_start_date.year
    # max_start_date_param = max_start_date.strftime("%x")
    max_start_date_param = f"{max_start_date_DD}/{max_start_date_MM}/{max_start_date_YYYY}"
    # print(f"Min start date: {min_start_date_param}, Max start date: {max_start_date_param}")
    getting_city_price = FlightSearch()
    try:
        ds_city_price = getting_city_price.find_city_price_0stop(dest_city_IATA_code, min_start_date_param, max_start_date_param)
        ds_via_city = ""
    except IndexError:
        try:
            print("Cannot find any price for 0 stop.")
            ds_city_price, ds_via_city = getting_city_price.find_city_price_1stop(dest_city_IATA_code, min_start_date_param, max_start_date_param)
        except IndexError:
            print("Error: Cannot find any price information even with one stopover.")
            ds_city_price = None
    sending_message = NotificationManager()
    try:
        if ds_city_price < dest_min_price:
            sending_message.send_emails(ds_city_price, 
                    ds_via_city,
                   depart_city_name = "London", 
                   depart_iata_code = "LON", 
                   dest_city_name = entry['city'], 
                   dest_iata_code = entry['iataCode'],
                   depart_date = min_start_date_param,
                   arrival_date = max_start_date_param)
    except TypeError:
        continue