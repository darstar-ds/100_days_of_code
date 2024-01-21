import requests
from pprint import pprint


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, sheety_auth_token, sheety_sheet_url):
        self.sheety_auth_token = sheety_auth_token
        self.sheety_sheet_url = sheety_sheet_url
        self.headers = {'Authorization': f'Bearer {sheety_auth_token}'}
    
    def get_prices(self):
        prices = requests.get(url=self.sheety_sheet_url, headers=self.headers)
        prices.raise_for_status()
        sheet_prices = prices.json()
        # pprint(sheet_prices)
        return sheet_prices
    
    def get_users(self):
        users = requests.get(url=self.sheety_sheet_url, headers=self.headers)
        users.raise_for_status()
        sheet_users = users.json()
        # pprint(sheet_prices)
        return sheet_users
    
    def insert_nu(self, nu_first_name, nu_last_name, nu_email):
        mod_url = self.sheety_sheet_url
        ds_nu = {
                        'user': {
                            'firstName': nu_first_name,
                            'lastName': nu_last_name,
                            'email': nu_email
                            }
                        }
        try:
            response = requests.post(url=mod_url, json=ds_nu, headers=self.headers)
            response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        except requests.exceptions.HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}') 
            print(f'Response body: {response.text}')
        except Exception as err:
            print(f'An error occurred: {err}')
        else:
            print("Your're in the Club")

