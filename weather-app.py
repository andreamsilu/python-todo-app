import requests
import json

# Replace 'API_KEY' with your actual OpenWeatherMap API key
API_KEY = '03c3df4d3139d6c3fd7bbf7afc67fc66'

def get_weather(city_name):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if data['cod'] == 200:
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            print(f"Weather in {city_name}:")
            print(f"Description: {weather_description.capitalize()}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(f"Error: {data['message']}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main():
    print("Welcome to the Weather App!")
    city_name = input("Enter the name of a city: ")
    get_weather(city_name)

if __name__ == "__main__":
    main()
