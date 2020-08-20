import requests
from requests.auth import HTTPBasicAuth

api_key = ""    # Your API Key
audio_file = "" # Your audio file path
url = "https://api-us.musiio.com/api/v1/upload/file"

files = [
  ('audio', open(audio_file,'rb'))
]

response = requests.post(url, auth=HTTPBasicAuth(api_key, ''), files = files)

print(response.text.encode('utf8'))
