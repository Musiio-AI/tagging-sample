import requests
from requests.auth import HTTPBasicAuth
import json

api_key = ""    # Your API Key
track_id = ""   # Track ID

url = "https://api-us.musiio.com/api/v1/extract/tags"

# You can customize tagging results by adding or removing query element from "tags" below
payload = {
    "id": track_id,
    "tags": ["CONTENT TYPE", "GENRE V3", "MOOD", "BPM", "KEY", "KEY SHARP", "ENERGY", "INSTRUMENTATION"]
}

headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, auth=HTTPBasicAuth(api_key, ''), headers=headers, data=json.dumps(payload))

print(response.text.encode('utf8'))
