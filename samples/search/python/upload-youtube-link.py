import requests
from requests.auth import HTTPBasicAuth
import json

api_key = ""  # Your API key here, required
youtube_link = ""   # YouTube link here, required
url = "https://api-us.musiio.com/v1/search/upload/youtube-link"

payload = {
    "link": youtube_link
}
headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, auth=HTTPBasicAuth(api_key, ''), headers=headers, data=json.dumps(payload))

print(response.text.encode('utf8'))
