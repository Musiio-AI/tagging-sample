import requests
from requests.auth import HTTPBasicAuth

api_key = ""  # Your API key here, required

url = "https://api-us.musiio.com/v1/catalog/info"

response = requests.get(url, auth=HTTPBasicAuth(api_key, ''))

print(response.text.encode('utf8'))
