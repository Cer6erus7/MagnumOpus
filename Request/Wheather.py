import requests
from apikey import API_TOKEN

params = {"q": "Vancouver", "appid":  API_TOKEN, "units": "metric"}

response = requests.get('https://api.openweathermap.org/data/2.5/weather?', params=params)

print(response.json())