import json
import ssl
from urllib.request import urlopen

def RetrieveData():
    url = "https://api.weather.gov/points/40.1933999,-85.3864"  # First Endpoint

    context = ssl._create_unverified_context()
    response = urlopen(url, context=context)
    weather_data = json.loads(response.read())

    forecast_url = weather_data["properties"]["forecast"]  # Gets the second URL from 'forecast'
    forecast_response = urlopen(forecast_url, context=context)
    forecast_data = json.loads(forecast_response.read())

    return forecast_data

forecast_data = RetrieveData()

for e in forecast_data["properties"]["periods"]:
    print(e["name"])
    print(e["temperature"])
    print(e["detailedForecast"])
    print()
        


    
