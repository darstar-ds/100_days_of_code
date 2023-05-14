import requests
import os
from datetime import datetime

USERNAME = "darstar2023"

pixela_endpoint = "https://pixe.la/v1/users"
pixela_token = os.environ.get("API_PIXELA_TOKEN")

user_params = {
    "token": pixela_token, 
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

'''
creating a user
'''
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "darstar1",
    "name": "Cycling Kilometers Graph",
    "unit": "km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": pixela_token,
}

'''
creating a graph
'''
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

point_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/darstar1"

optionalDataDS = {
    "DS1": "1",
    "DS2": "2",
    "DS3": "3",
}

today = datetime(year=2023, month=5, day=13)
# print(today.strftime("%Y%m%d"))
formated_date = today.strftime("%Y%m%d")

point_config = {
    "date": formated_date,
    "quantity": "10.9",
    # "optionalData": optionalDataDS,
}

'''
posting a pixel
'''
# response = requests.post(url=point_endpoint, json=point_config, headers=headers)
# print(response.text)

'''
updating a pixel
'''
point_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/darstar1/{formated_date}"

point_update_config = {
    "quantity": "2.5",
}

# response = requests.put(url=point_update_endpoint, json=point_update_config, headers=headers)
# print(response.text)

'''
deleting a pixel
'''
point_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/darstar1/{formated_date}"

response = requests.delete(url=point_delete_endpoint, headers=headers)
print(response.text)


