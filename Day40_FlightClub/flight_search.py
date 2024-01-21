import os
import requests
import json
from pprint import pprint

kiwi_api_key = os.environ.get("API_KIWI_KEY")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    # def __init__(self) -> None:
 
    def get_iataCode(self, city):
        json_params = {
                    'term': city, 
                    'location_types': 'city'
                    }
        headers = {
                    'apikey': kiwi_api_key,
                    }
        tequilla_url = f'https://api.tequila.kiwi.com/locations/query'
        try:
            response = requests.get(url=tequilla_url, params=json_params, headers=headers)
            response.raise_for_status()
            pprint(response.text)
            ds_response = response.json()["locations"]
            ds_iataCode = ds_response[0]['code']
            print(ds_iataCode)
            return ds_iataCode
            
        except requests.exceptions.HTTPError as errh:
            print(f"Http Error: {errh}")  # Handle HTTP errors like 400 Bad Request
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")  # Handle connection-related errors
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")  # Handle timeout errors
        except requests.exceptions.RequestException as err:
            print(f"An Unknown Error Occurred: {err}")  # Handle any other errors

        else:
            print('Success!')

        
    def find_city_price_0stop(self, dest_city_IATA_code, min_start_date, max_start_date):
        json_params = {
                    'fly_from': 'LON',
                    'fly_to': dest_city_IATA_code,
                    'date_from': min_start_date,
                    'date_to': max_start_date,
                    # 'return_from': 
                    # 'return_to'
                    'nights_in_dst_from': 7,
                    'nights_in_dst_to': 28,
                    'curr': 'GBP',
                    'max_stopovers': 0
                    }
        headers = {
                    'apikey': kiwi_api_key,
                    }
        tequilla_url = f'https://api.tequila.kiwi.com/search'
        try:
            # print(f"Min start date: {min_start_date}, Max start date: {max_start_date}")
            response = requests.get(url=tequilla_url, params=json_params, headers=headers)
            response.raise_for_status()
            ds_response = response.json()["data"]

            # pprint(response.text)
            filename = r"C:\Users\dariu\OneDrive\Dokumenty\Python Scripts\100_days_of_code\Day40_FlightClub\0stop_json.txt"
            with open(filename, 'w') as outfile:
                json.dump(ds_response, outfile)

            ds_city_price = ds_response[0]['price']
            print(f"{dest_city_IATA_code}: {ds_city_price} GBP")
            return ds_city_price
            
        except requests.exceptions.HTTPError as errh:
            print(f"Http Error: {errh}")  # Handle HTTP errors like 400 Bad Request
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")  # Handle connection-related errors
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")  # Handle timeout errors
        except requests.exceptions.RequestException as err:
            print(f"An Unknown Error Occurred: {err}")  # Handle any other errors

        else:
            print('Success! Found a price with no stopovers.')

    def find_city_price_1stop(self, dest_city_IATA_code, min_start_date, max_start_date):
        json_params = {
                    'fly_from': 'LON',
                    'fly_to': dest_city_IATA_code,
                    'date_from': min_start_date,
                    'date_to': max_start_date,
                    'nights_in_dst_from': 7,
                    'nights_in_dst_to': 28,
                    'curr': 'GBP',
                    'stopovers': 1,
                    'via_city' : "",
                    }
        headers = {
                    'apikey': kiwi_api_key,
                    }
        tequilla_url = f'https://api.tequila.kiwi.com/search'
        try:
            # print(f"Min start date: {min_start_date}, Max start date: {max_start_date}")
            response = requests.get(url=tequilla_url, params=json_params, headers=headers)
            response.raise_for_status()
            ds_response = response.json()["data"]
        
            # pprint(response.text)
            filename = r"C:\Users\dariu\OneDrive\Dokumenty\Python Scripts\100_days_of_code\Day40_FlightClub\1stop_json.txt"
            with open(filename, 'w') as outfile:
                json.dump(ds_response, outfile)

            ds_city_price = ds_response[0]['price']
            ds_via_city = ds_response[0]['route'][2]['cityFrom']
            print(f"{dest_city_IATA_code}: {ds_city_price} GBP")
            return ds_city_price, ds_via_city
            
        except requests.exceptions.HTTPError as errh:
            print(f"Http Error: {errh}")  # Handle HTTP errors like 400 Bad Request
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")  # Handle connection-related errors
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")  # Handle timeout errors
        except requests.exceptions.RequestException as err:
            print(f"An Unknown Error Occurred: {err}")  # Handle any other errors

        else:
            print('Success! Found a price with one stopover.')
        