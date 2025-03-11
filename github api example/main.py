import os
import requests
from dotenv import load_dotenv


load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") # 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
if not GITHUB_TOKEN:
    raise ValueError("Missing GITHUB_TOKEN")

OWNER = "MagicMannnnn"
REPO = "Python-Course"

API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/contents"

# Headers for OAuth2 authentication
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}


def list_files(path=""):
    url = f"{API_URL}/{path}" if path else API_URL  # If path is provided build the URL
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.json().get('message', 'Unknown error')}")
        return

    items = response.json()

    for item in items:

        if item['type'] == 'file':
            print(f"File: {item['name']} - {round(item['size']/1000, 1)}KB")

        elif item['type'] == 'dir':
            print(f"Entering directory: {item['name']}")
            list_files(item['path'])  # Recurse into directory


if __name__ == "__main__":
    list_files()
