import os
import requests
import logging
from dotenv import load_dotenv

# Set up logging
logger = logging.getLogger('WeatherApp')
logging.basicConfig(
    filename='weatherstack.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)

# Load API key from environment
load_dotenv()
API_KEY = os.getenv('WEATHERSTACK_API_KEY')
if not API_KEY:
    logger.critical("WEATHERSTACK_API_KEY not found in environment variables.")
    raise EnvironmentError("Missing WEATHERSTACK_API_KEY in environment variables.")

def get_weather(city):
    logger.info(f"Fetching weather for: {city}")
    url = "http://api.weatherstack.com/current"
    params = {
        "access_key": API_KEY,
        "query": city
    }

    try:
        response = requests.get(url, params=params)
        logger.debug(f"Request URL: {response.url}")
        response.raise_for_status()
        data = response.json()
        print(data)

        if "error" in data:
            logger.error(f"API Error: {data['error']}")
            print("API error. Check your query or key.")
            return

        location = data['location']['name']
        temp = data['current']['temperature']
        description = data['current']['weather_descriptions'][0]
        logger.info(f"Weather in {location}: {temp}°C, {description}")
        print(f"The temperature in {location} is {temp}°C with {description}.")

    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")
        print("Failed to get weather data.")
    except Exception as e:
        logger.exception("An unexpected error occurred.")
        print("Unexpected error.")


if __name__ == "__main__":
    logger.info("Weatherstack script started")
    city_name = input("Enter a city: ")
    get_weather(city_name)
    logger.info("Weatherstack script finished")
