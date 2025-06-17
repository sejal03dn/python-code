import requests

def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # For temperature in Celsius
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        print(f"\nWeather in {city}:")
        print(f"Condition: {weather}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%\n")
    else:
        print("City not found or something went wrong.")

# Replace with your actual API key
api_key = "YOUR_API_KEY_HERE"
city = input("Enter a city name: ")
get_weather(city, api_key)
