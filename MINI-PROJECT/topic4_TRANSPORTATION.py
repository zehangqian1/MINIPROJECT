# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 01:32:03 2024

@author: zehan
"""

import requests
import pandas as pd
# URL for Bus Services API
url = "http://datamall2.mytransport.sg/ltaodataservice/BusServices"

# Headers with API key for authentication
headers = {
    'AccountKey': '5ZbLEkLlRU+VLuijhDLlZA==',  # Your API key
    'accept': 'application/json',  # Accept JSON format
}

# Send GET request
response = requests.get(url, headers=headers)

# Print the response
print(response.text)
data=response.json()

df = pd.DataFrame(data['value'])
df.to_csv('transportation.csv', index=True)








# import requests
# import csv
# import json

# # URL for Bus Services API
# url = "http://datamall2.mytransport.sg/ltaodataservice/BusServices"

# # Headers with API key for authentication
# headers = {
#     'AccountKey': '5ZbLEkLlRU+VLuijhDLlZA==',  # Your API key
#     'accept': 'application/json',  # Accept JSON format
# }

# # Send GET request
# response = requests.get(url, headers=headers)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the JSON response
#     data = response.json()
    
#     # Open a CSV file to write the data
#     with open('bus_services.csv', mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
        
#         # Write the header row (adjust this based on the actual structure of your data)
#         writer.writerow(['ServiceNo', 'Operator', 'Category', 'OriginCode', 'DestinationCode'])
        
#         # Write the bus services data
#         for service in data['value']:
#             writer.writerow([
#                 service['ServiceNo'],
#                 service['Operator'],
#                 service['Category'],
#                 service['OriginCode'],
#                 service['DestinationCode']
#             ])
    
#     print("Data saved to bus_services.csv")
# else:
#     print(f"Failed to fetch data. Status code: {response.status_code}")
