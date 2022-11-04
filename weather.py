
import requests
from pprint import pprint       #pretty print
import json

#using open weather API
api_key = "input your own api key here..."
city = input('Enter a city:')
def main():
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="+str(city)+"&appid="+api_key

    weather_data = requests.get(base_url).json()
    print(weather_data)
    pprint(weather_data)

if __name__ == '__main__':
    main()
        
