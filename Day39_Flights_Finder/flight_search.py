import os
import requests

kiwi_api_key = os.environ.get("API_KIWI_KEY")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city) -> None:
        self.city = city
 
    def get_iataCode(self):
        json_params = {
                    'term': self.city, 
                    'location_types': 'city'
                    }
        headers = {
                    'apikey': kiwi_api_key,
                    }
        tequilla_url = f'https://api.tequila.kiwi.com/locations/query'
        try:
            response = requests.get(url=tequilla_url, params=json_params, headers=headers)
            response.raise_for_status()
            print(response.text)
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

        
        