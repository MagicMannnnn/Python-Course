import requests
import logging

# this is an alternate way to log stuff

logging.basicConfig(filename='requests_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

url = "https://www.example.com"

try:
    response = requests.get(url)

    response.raise_for_status()

    # Check if the request was successful
    if response.status_code == 200:
        logging.info("Successfully fetched the webpage.")
        logging.info(f"Status Code: {response.status_code}")
        print("Page fetched successfully!")
    else:
        logging.warning(f"Failed to fetch the webpage. Status Code: {response.status_code}")
        print("Failed to fetch the page.")
except requests.exceptions.RequestException as e:
    logging.error(f"Request failed: {e}")
    print("There was an error with the request.")
