import requests

url = "https://www.example.com"

response = requests.get(url)

if response.status_code == 200:
    print("Successfully fetched the webpage!")
    print("Status Code:", response.status_code)
    print("First 500 characters of content:")
    print(response.text[:500])
else:
    print("Failed to fetch the webpage. Status code:", response.status_code)
