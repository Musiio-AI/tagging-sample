import requests
from requests.auth import HTTPBasicAuth

api_key = ""  # Your API key here, required
track_id = ""   # Your track ID to be updated, required

url = "https://api-us.musiio.com/v1/catalog/track"

payload = {
    'id': track_id,
    'primary_customer_track_id': '',
    'version': '',
    'title': '',
    'album': '',
    'artist': '',
    'year': '',
    'region': '',
    'language': '',
    'explicit': '',
    'genres': '',
    'moods': '',
    'style': '',
    'instruments': '',
    'description': '',
    'keywords': ''
}

response = requests.put(url, data=payload, auth=HTTPBasicAuth(api_key, ''))

print(response.text.encode('utf8'))
