# Weather App

This is a simple command line weather application that fetches current weather data from [Open-Meteo](https://open-meteo.com/).

## Setup

1. Create a virtual environment (optional):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with latitude and longitude as arguments. If no arguments are provided, it defaults to New York City.

```bash
python weather.py 52.52 13.41
```

