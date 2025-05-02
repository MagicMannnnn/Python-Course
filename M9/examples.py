import requests
import logging

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Example of a GET request using the requests library
def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        logging.info(f"Successful request to {url}")
        return response.json()  # Return JSON data if the request was successful

    except requests.exceptions.HTTPError as err: # error during request
        logging.error(f"HTTP error occurred: {err}")
        return None

    except Exception as err: # error during code
        logging.error(f"Other error occurred: {err}")
        return None

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/posts'  # Example URL
    data = fetch_data_from_api(url)
    logging.warning("this is a test warning")
    if data:
        for i in data: # dictionary
            print("\n\n")
            for key, value in zip(i.keys(), i.values()):
                print(f"key: {key}, value: {value}")
            #print(i)

