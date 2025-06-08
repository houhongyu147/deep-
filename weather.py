import requests
import sys

API_URL = "https://api.open-meteo.com/v1/forecast"


def fetch_weather(lat: float, lon: float) -> dict:
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
    }
    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def format_weather(data: dict) -> str:
    current = data.get("current_weather", {})
    temp = current.get("temperature")
    windspeed = current.get("windspeed")
    time = current.get("time")
    if temp is None:
        return "Weather data unavailable"
    return f"Temperature: {temp}°C\nWind Speed: {windspeed} km/h\nTime: {time}"


def main(argv):
    if len(argv) >= 3:
        lat = float(argv[1])
        lon = float(argv[2])
    else:
        lat = 40.7128  # Default: New York City
        lon = -74.0060
    data = fetch_weather(lat, lon)
    print(format_weather(data))


if __name__ == "__main__":
    main(sys.argv)

