import requests
import logging
import os
import datetime
from dotenv import load_dotenv
import urllib3

# Suppress the annoying certificate warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load environment variables from .env file
load_dotenv()
baseURL = os.getenv('base_url')
clientID = os.getenv('client_id')
clientSecret = os.getenv('client_secret')
userID = os.getenv('userID')
password = os.getenv('password')
scope = os.getenv('scope')

# Gather basic script info
nameOfScript = os.path.basename(__file__)  # Grab the name of the file
scriptPID = os.getpid()  # Get the process ID of the script

# Generate date(s) that we might want
today = datetime.datetime.today()
dateNow = today.strftime("%d-%m-%Y")

# Create logging framework
log_level = logging.DEBUG  # Define the global logging level
logger = logging.getLogger(nameOfScript)
logger.setLevel(log_level)  # Set the global logging level

# Create file handler for logging
logFileName = f'{nameOfScript} - {dateNow}.log'  # add str(scriptPID) for per-instance logging
loggingFormat = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

fileLogHandler = logging.FileHandler(logFileName)  # Create handler for logging to file
fileLogHandler.setLevel = log_level  # Set file handler logging level to common logging level

# Set logfile format
fileLogHandler.setFormatter(loggingFormat)

# Add file handler to logging
logger.addHandler(fileLogHandler)


# Log in to iManage Work using Oauth2
def log_in(headers):
    parameters = {
        'username': userID,
        'password': password,
        'grant_type': 'password',
        'client_id': clientID,
        'client_secret': clientSecret,
        'scope': scope
    }
    response = requests.post(f'https://{baseURL}/auth/oauth2/token', headers=headers, data=parameters, verify=False)
    json_response = response.json()
    if response.ok:
        logger.info('Login Successful')
        return json_response['access_token']
    else:
        logger.error(f'Sign in failed: {json_response["error_description"]}')
        logger.error('Exiting...')
        exit()


# Log out of iManage Work
def log_out():
    response = requests.get(f'https://{baseURL}/auth/logout', verify=False)
    if response.ok:
        logger.info('Logged Out.')
    else:
        json_response = response.json()
        logger.error(f'Sign out failed: {json_response["error_description"]}')


# Get customer (tenant) ID
def get_customer_id(headers):
    response = requests.get(f'https://{baseURL}/api', headers=headers, verify=False)
    json_response = response.json()
    customer_id = str(json_response['data']['user']['customer_id'])
    logger.info(f'Logged in with user:{json_response["data"]["user"]["email"]} Tenant ID: {customer_id}')
    return customer_id


# Example function that gets document details from iManage Work and prints the doc numbers
def get_docs(x_headers, customer_id, library):
    logger.info(f'Getting document info from {library}')
    response = requests.get(f'https://{baseURL}/work/api/v2/customers/{customer_id}/libraries/{library}/documents',
                            headers=x_headers, verify=False)
    parsed_response = response.json()
    logger.info(f'Response received from {baseURL} - {len(parsed_response["data"]["results"])} results received')
    for doc in parsed_response['data']['results']:
        print(doc['document_number'])


def main():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    x_auth_token = log_in(headers)
    x_headers = {'X-Auth-Token': x_auth_token}
    customer_id = get_customer_id(x_headers)
    get_docs(x_headers, customer_id, 'Room101')
    log_out()


if __name__ == '__main__':
    main()
