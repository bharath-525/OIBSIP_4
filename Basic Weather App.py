import requests

def get_weather(api_key, location):
    # Define the API endpoint and parameters
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    # Make the API request
    response = requests.get(url, params=params)
    
    # Check for a valid response
    if response.status_code == 200:
        data = response.json()
        weather = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'conditions': data['weather'][0]['description']
        }
        return weather
    else:
        return None

def main():
    # Get your API key from OpenWeatherMap
    api_key = "8baf980d5d87bee4c8a3a4ae42802f90"

    print("Weather App")

    # Get user input for location
    location = input("Enter city or ZIP code: ")

    # Fetch weather data
    weather = get_weather(api_key, location)
    
    # Display weather data
    if weather:
        print(f"Current weather in {location.capitalize()}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Conditions: {weather['conditions'].capitalize()}")
    else:
        print("Error: Unable to fetch weather data. Please check your location and try again.")

if __name__ == "__main__":
    main()
