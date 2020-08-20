import requests
from requests.auth import HTTPBasicAuth
import json

api_key = ""  # Your API key here, required
track_id = ""   # Track ID here, required
search_text = ""    # Your search text here
page = 0    # Page number
items = 50  # Number of items to show per page

url = "https://api-us.musiio.com/v1/search/perform"

payload = {
    "id": track_id,
    "text": search_text,
    "page": page,
    "items": items
}

headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, auth=HTTPBasicAuth(api_key, ''), headers=headers, data=json.dumps(payload))

print(response.text.encode('utf8'))
