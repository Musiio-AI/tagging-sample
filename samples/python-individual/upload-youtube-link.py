import requests
from requests.auth import HTTPBasicAuth
import json

api_key = ""    # Your API Key
youtube_link = "" # Your YouTube link

url = "https://api-us.musiio.com/api/v1/upload/youtube-link"

payload = {
    "link": youtube_link
}

headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=json.dumps(payload), auth=HTTPBasicAuth(api_key, ''))

print(response.text.encode('utf8'))
