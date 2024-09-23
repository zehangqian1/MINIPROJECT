# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 23:59:00 2024

@author: zehan
"""



import requests
import pandas as pd

url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=10"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmMjRjYjM2YzkxYjI1MDE2NDBjYzAwZDYzOWFiNTdkYSIsIm5iZiI6MTcyNzAyMDg2NC43MTE5MjIsInN1YiI6IjY2ZjAzODQ0NmMzYjdhOGQ2NDhkODIyMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.abO2QpkMaE8MMnKv0HeFota3tzQ6zYY2IDh58uBQSvU"
}

response = requests.get(url, headers=headers)
data = response.json()
df = pd.DataFrame(data['results'])
df.to_csv('movies.csv', index=True)
# print(response.text)