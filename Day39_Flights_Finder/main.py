#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

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

for entry in sheet_data['prices']:
    city_name = entry['city']
    row_id = entry['id']
    getting_code = FlightSearch(city_name)
    ds_iataCode = getting_code.get_iataCode()
    inserting_code = DataManager(sheety_auth_token, sheety_sheet_url)
    insert_code = inserting_code.insert_iataCode(ds_iataCode, row_id)

