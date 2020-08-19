import requests
from requests.auth import HTTPBasicAuth

api_key = ""  # Your API key here, required
audio_file = "" # Your audio file path here, required

url = "https://api-us.musiio.com/v1/catalog/track"

# you can customize track information but fill up the remaining empty fields below
payload = {
  'customer_track_id': '',
  'primary_customer_track_id': '',
  'version': '',
  'title': '',
  'album': '',
  'artist': '',
  'year': '',
  'region': '',
  'language': '',
  'explicit': '',
  'genre': '',
  'moods': '',
  'style': '',
  'instruments': '',
  'description': '',
  'keywords': ''
}
files = [
  ('track', open(audio_file,'rb'))
]

response = requests.post(url, data=payload, files=files, auth=HTTPBasicAuth(api_key, ''))

print(response.text.encode('utf8'))