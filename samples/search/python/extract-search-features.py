import requests
from requests.auth import HTTPBasicAuth
import json

api_key = ""  # Your API key here, required
track_id = ""   # Track ID here, required

url = "https://api-us.musiio.com/v1/search/extract/search-features"

payload = {
    "id": track_id
}

headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, auth=HTTPBasicAuth(api_key, ''), headers=headers, data=json.dumps(payload))

print(response.text.encode('utf8'))
