import requests
from requests.auth import HTTPBasicAuth

api_key = ""  # Your API key here, required
track_id = ""   # Your track ID here
url = "https://api-us.musiio.com/v1/catalog/track?id=" + track_id

response = requests.get(url, auth=HTTPBasicAuth(api_key, ''))

print(response.text.encode('utf8'))
