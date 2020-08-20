import requests
from requests.auth import HTTPBasicAuth

api_key = ""  # Your API key here, required
audio_file = "" # Your audio file path here, required
url = "https://api-us.musiio.com/v1/search/upload/file"

files = [
  ('audio', open(audio_file,'rb'))
]


response = requests.post(url, auth=HTTPBasicAuth(api_key, ''), files = files)

print(response.text.encode('utf8'))
