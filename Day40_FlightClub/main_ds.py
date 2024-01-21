#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from pprint import pprint
from data_manager import DataManager
# from flight_search import FlightSearch
# from notification_manager import NotificationManager
from datetime import timedelta, datetime

sheety_auth_token = os.environ.get("API_SHEETY_AUTH_TOKEN")
sheety_prices_sheet_url = "https://api.sheety.co/e598720cc327978305991b5be8ed94dc/dsFlightDeals/prices"
sheety_users_sheet_url = "https://api.sheety.co/e598720cc327978305991b5be8ed94dc/dsFlightDeals/users"

obj_prices = DataManager(sheety_auth_token, sheety_prices_sheet_url)
sheet_data_prices = obj_prices.get_prices()
pprint(sheet_data_prices)

obj_users = DataManager(sheety_auth_token, sheety_users_sheet_url)
sheet_data_users = obj_users.get_users()
pprint(sheet_data_users)

def get_new_user_data():
    nu_first_name = input("What is your first name?\n") 
    nu_last_name = input("What is your last name?\n")
    nu_email = input("What is your e-mail?\n")
    nu_email2 = input("Type your e-mail again.\n")
    while nu_email != nu_email2:
        print("The emails do not match. Please try again.\n")
        nu_email = input("What is your e-mail?\n")
        nu_email2 = input("Type your e-mail again.\n")
    
    return nu_first_name, nu_last_name, nu_email

def verify_email(nu_email, sheet_data_users):
    is_user_in_club = False
    for entry in sheet_data_users['users']:
        existing_email = entry['email']
        # print(f"existing email: {existing_email}")
        nu_email = nu_email
        # print(f"new email: {nu_email}")
        # print(f"is_user_in_club: {is_user_in_club}")
        if existing_email == nu_email:
            # print("The user with the provided e-mail already exists")
            is_user_in_club = True
            # print(f"is_user_in_club: {is_user_in_club}")
            break
    # print(f"is_user_in_club: {is_user_in_club}")
    return is_user_in_club


print("Welcome to Darek's Flight Club.\nWe find the best flight deals and email you.\n")
nu_first_name, nu_last_name, nu_email = get_new_user_data()  
is_user_in_club = verify_email(nu_email, sheet_data_users)
if is_user_in_club == False:
    obj_users.insert_nu(nu_first_name, nu_last_name, nu_email)
