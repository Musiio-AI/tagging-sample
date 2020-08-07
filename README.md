# Musiio Tagging Sample

Sample codes for generating tags using Musiio Tagging Service, from given audio tracks source or youtube links.

## Samples
Samples are separated according to different languages. Currently `PHP` and `Python` are supported. They are stored respectively under `samples/php/` and `samples/py/` folders
### PHP sample
`audio-upload.php`\
Open the file, replace `$apiKey` `$audioPath` with your own API key and the local path that stores the audio file. This script uploads the audio files in the folder onto Musiio Tagging Service. To run:
```bash
php audio-upload.php
```
The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.
___
`youtube-upload.php`\
Open the file, replace `$apiKey` `$youtubeUrl` with your own API key and the youtube track link. This script upload the youtube track onto Musiio Tagging Service. To run:
```bash
php youtube-upload.php
```
The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.
___
`extract-tags.php`\
Open the file, replace `$apiKey` `$trackId` with your own API key and the Track ID generated after the upload. This script will run the Tagging Service and return the tagging results in the console.
```bash
php extract-tags.php
```
The response will be printed out in the console.
### Python sample
**Python version:** 3.6.8\
`generate_tags.py`\
tag audio tracks located in a given folder and save tags in .json format for each track\
`tags_to_csv.py`\
check all tag .json files located in a given folder and write the tags to a single CSV file\
`constants.py`\
update the values of 'KEY' and 'BASE_URL' with your Musiio API Key and API Url\


#### Installation
```bash
cd samples\py
virtualenv venv
cd venv\scripts
activate
cd ..\..
pip install -r requirements
```

#### Update constants.py with API Key
```python
KEY = "Replace With Your Musiio API KEY"
BASE_URL = "Replace with Your API URL"
```

#### Tag Generation

```bash
python generate_tags.py --source-path C:/tagging_scripts/tracks --destination-path C:/tagging_scripts/tags --tag-selection "content type" "genre" "bpm" "key" "mood" "energy" "instrumentation"
```

#### Convert Tags to CSV
```bash
python tags_to_csv.py --tags-path C:/tagging_scripts/tags --tags-csv C:/tagging_scripts --tags-types "genre" "genre secondary" "mood" "mood secondary" "energy" "vocal presence" "instrument"
```


### Windows Executable GUI Usage

Executables are located in the `windows` folder\
**Note:** GUI applications for MacOS are currently not available for distribution, but you should be able to build them yourself using the instructions below under 'Rebuilding the GUI'

#### Tag Generation

**Source Folder:** The folder where your audio tracks are stored\
**Destination Folder:** The folder where you want your tag jsons to be saved\
**API Key:** Replace with your Musiio API Key


#### Convert Tags to CSV

**Tag Folder:** The folder containing your tag jsons\
**Write CSV to Directory:** The folder where the CSV will be saved

### Rebuilding the GUI

#### Windows
```bash
pip install pyinstaller
pyinstaller --onefile generate_tags_gui.py
```
#### Mac
```bash
pip install py2app==0.13
```

Create setup.py as follows:

```python
from setuptools import setup

APP = ['generate_tags_gui.py']
DATA_FILES = []
OPTIONS = {
    'iconfile': 'images/generate_tags.icns',
    'argv_emulation': True,
    'packages': ['certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
```
```bash
python setup.py py2app
```
Replace 'APP' and 'iconfile' variables accordingly and follow the same steps for tags_to_csv_gui.py
