# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:16:14 2024

@author: zehan
"""

# 6D8LMYCTK3FFRV6O
# import requests
# import pandas as pd
# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=6D8LMYCTK3FFRV6O'
# r = requests.get(url)
# data = r.json()
# # Convert the list of movies into a DataFrame
# df = pd.DataFrame(data['Time Series (5min)'])
# print(data)
# df.to_csv('IBM_5min_intraday.csv')



# import requests
# import pandas as pd
# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=1min&apikey=6D8LMYCTK3FFRV6O'
# r = requests.get(url)
# data = r.csv()
# # Convert the list of movies into a DataFrame
# df = pd.DataFrame(data['Time Series (1min)'])
# print(data)
# df.to_csv('IBM_1min_intraday.csv')




import requests

# API URL with 1-minute interval for intraday data and CSV format
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=1min&apikey=6D8LMYCTK3FFRV6O&datatype=csv'

# Send the GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the response content (CSV data) to a file
    with open('IBM_1min_intradaycsv.csv', 'wb') as file:
        file.write(response.content)

    print("Data saved to IBM_1min_intradaycsv.csv")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

