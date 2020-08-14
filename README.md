# Musiio Code Sample

Sample codes for generating tags using Musiio Tagging Service, from given audio tracks source or youtube links.

[TOC]

## Tagging Samples

This is a sample collection for uploading tracks and extract tags from them. It can be found under `samples/tagging/`
### Postman Collection

If you don't have postman, download here: https://www.postman.com/downloads/

Here is the collection public link:

https://www.getpostman.com/collections/2d47eb75d66a50ed4308

#### How to set up postman samples

1. Download postman and install it.
2. Open postman, at the top left corner click on "Import" button
3. Choose "Link" tab
4. Copy paste the collection public link in and click "Continue"
5. Press "Import" to import the collection
6. You will see the collection folder appears on the left-side panel. Click to expand to see individual request query.
7. Now you need to add your API key in to authorize your request. Click on the "three dots" icon on the right of the collection folder tab when your mouse hovers on it. Click "Edit". Under the "Authorization" tab, select "Basic Auth" and copy paste your **Tagging API key** into the "username" field. Leave the "password" field empty. Click "Update" to update your collection.
8. Now you are all set and it is time to use the sample.

#### Upload Audio File

1. Click on "Upload Audio File" query under your collection. On the main panel, click on "Body" and select "form-data"
2. Input KEY as "audio" and press "Select Files" under VALUE to select an audio file to be uploaded
3. Press "**Send**" to send the request.
4. You will receive response at the bottom panel

#### Upload YouTube Link

1. Click on "Upload YouTube Link" query under your collection. On the main panel, click on "Body" and select "raw", on the right select "JSON" in the dropdown menu.
2. Input the following into the textbox:

   ```json
   {
   	"link": "YOUR YOUTUBE LINK HERE"
   }
   ```

3. Press "**Send**" to send the request.
4. You will receive response at the bottom panel

#### Upload Audio Link

1. Click on "Upload Audio Link" query under your collection. On the main panel, click on "Body" and select "raw", on the right select "JSON" in the dropdown menu.
2. Input the following into the textbox:

   ```json
   {
   	"link": "YOUR AUDIO LINK HERE"
   }
   ```
3. Press "**Send**" to send the request.
4. You will receive response at the bottom panel

#### Extract Tags

1. Click on "Extract Tags" query under your collection. On the main panel, click on "Body" and select "raw", on the right select "JSON" in the dropdown menu.
2. Input the following into the textbox:

   ```json
   {
       "id": "TRACK ID HERE",
       "tags": ["CONTENT TYPE", "GENRE V3", "MOOD", "BPM", "KEY", "KEY FLAT", "KEY SHARP", "ENERGY", "INSTRUMENTATION", "HIT POTENTIAL"]
   }
   ```
   You can add or remove tags from the array in the sample above to customize the tags you want to receive
3. Press "**Send**" to send the request.
4. You will receive response at the bottom panel

### PHP sample

#### Upload Audio File

`audio-upload.php`\
Open the file, replace `$apiKey` `$audioPath` with your own API key and the local path that stores the audio file. This script uploads the audio files in the folder onto Musiio Tagging Service. To run:

```bash
php audio-upload.php
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

#### Upload YouTube Link

`youtube-upload.php`\
Open the file, replace `$apiKey` `$youtubeUrl` with your own API key and the youtube track link. This script upload the youtube track onto Musiio Tagging Service. To run:

```bash
php youtube-upload.php
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

#### Upload Audio Link

`upload-audio-link.php`\
Open the file, replace `$apiKey` `$audioLink` with your own API key and the youtube track link. This script upload the youtube track onto Musiio Tagging Service. To run:

```bash
php upload-audio-link.php
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

#### Extract Tags

`extract-tags.php`\
Open the file, replace `$apiKey` `$trackId` with your own API key and the Track ID generated after the upload. This script will run the Tagging Service and return the tagging results in the console.

```bash
php extract-tags.php
```

The response will be printed out in the console.

### Python individual sample

The folder `samples/tagging/python-individual` contains scripts that handle individual track tagging

#### Set up running environment

To install all the dependencies necessary for the scripts. Run the following code in your terminal:

For Mac

```bash
cd samples/tagging/python-individual
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

For Windows

```bash
cd samples\tagging\python-individual
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```

To deactivate virtual environment

```bash
deactivate
```

#### 

#### Upload Audio File

`upload-audio-file.py`

Input required `api_key`, `audio_file`. 

To run:

```bash
python upload-audio-file.py
```

#### Upload YouTube Link

`upload-youtube-link.py`

Input required `api_key`, `youtube_link`. 

To run:

```bash
python upload-youtube-link.py
```

#### Upload Audio Link

`upload-audio-link.py`

Input required `api_key`, `audio_link`. 

To run:

```bash
python upload-audio-link.py
```

#### Extract Tags

`extract-tags.py`

Input required `api_key`, `track-id`. 

Available tags: 

`["CONTENT TYPE", "GENRE V3", "MOOD", "BPM", "KEY", "KEY SHARP", "ENERGY", "INSTRUMENTATION"]`

To run:

```bash
python extract-tags.py
```

### Python Integrated sample

The folder `samples/tagging/python-integrated` contains scripts that take multiple audio tracks in one folder and tag them one-by-one and output into CSV file.

**Python version:** 3.6.8
`generate_tags.py`
tag audio tracks located in a given folder and save tags in .json format for each track\
`tags_to_csv.py`
check all tag .json files located in a given folder and write the tags to a single CSV file\
`constants.py`
update the values of 'KEY' and 'BASE_URL' with your Musiio API Key and API Url\

#### Installation

```bash
cd samples\tagging\python-integrated
virtualenv venv
venv\Scripts\activate
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

## Search Samples

This is a sample collection for uploading tracks and extract tags from them. It can be found under `samples/search/`

### Postman Collection

If you don't have postman, download here: https://www.postman.com/downloads/

Here is the collection public link:

https://www.getpostman.com/collections/9fc329fc3c4bf6b7af6c

#### How to set up postman samples

1. Download postman and install it.
2. Open postman, at the top left corner click on "Import" button
3. Choose "Link" tab
4. Copy paste the collection public link in and click "Continue"
5. Press "Import" to import the collection
6. You will see the collection folder appears on the left-side panel. Click to expand to see individual request query.
7. Now you need to add your API key in to authorize your request. Click on the "three dots" icon on the right of the collection folder tab when your mouse hovers on it. Click "Edit". Under the "Authorization" tab, select "Basic Auth" and copy paste your **Search API key** into the "username" field. Leave the "password" field empty. Click "Update" to update your collection.
8. Now you are all set and it is time to use the sample.

#### Add Track

1. Click on "Add Track" query under your collection. On the main panel, click on "Body" and select "form-data"
2. Under "track" click on "Select Files" under VALUE to select your audio file. Please input **required** "customer_filename" as well.
3. Fill up remaining track information if needed to.
4. Press "**Send**" to send the request.
5. You will receive response at the bottom panel

#### Update Track

1. Click on "Update Track" query under your collection. On the main panel, click on "Body" and select "form-data".
2. Input the values you want to update.
3. Press "**Send**" to send the request.
4. You will receive response at the bottom panel.

#### Get Track

1. Click on "Get Track" query under your collection. On the main panel, click on "Params"
2. Input the the **id** of the track that you want to get.
3. Press "**Send**" to send the request.
4. You will receive response at the bottom panel

#### Delete Track

1. Click on "Delete Track" query under your collection. On the main panel, click on "Params"
2. Input the **id** of the track that you want to delete.
3. Press "**Send**" to send the request.
4. You will receive response at the bottom panel

#### Catalog Info

1. Click on "Catalog Info" query under your collection.
2. Press "**Send**" to send the request.
3. You will receive response at the bottom panel

#### Upload File

1. Click on "Upload File" query under your collection. On the main panel, click on "Body" and select "form-data"
2. Input KEY as "audio" and press "Select Files" under VALUE to select an audio file to be uploaded
3. Press "**Send**" to send the request.
4. You will receive response at the bottom panel

#### Upload YouTube Link

1. Click on "Upload YouTube Link" query under your collection. On the main panel, click on "Body" and select "raw", on the right select "JSON" in the dropdown menu.

2. Input the following into the textbox:

   ```json
   {
   	"link": "YOUR YOUTUBE LINK HERE"
   }
   ```

   

3. Press "**Send**" to send the request.

4. You will receive response at the bottom panel

#### Extract Search Features

1. Click on "Extract Search Features" query under your collection. On the main panel, click on "Body" and select "raw", on the right select "JSON" in the dropdown menu.

2. Input the following into the textbox:

   ```json
   {
       "id": "TRACK ID HERE"
   }
   ```

3. Press "**Send**" to send the request.

4. You will receive response at the bottom panel

#### Perform Search

1. Click on "Perform Search" query under your collection. On the main panel, click on "Body" and select "raw", on the right select "JSON" in the dropdown menu.

2. Input the following into the textbox:

   ```json
   {
   	"id": "Input track ID here",
   	"text": "Input search text here",
   	"page": 0,
   	"items": 50
   }
   ```

3. Press "**Send**" to send the request.

4. You will receive response at the bottom panel

#### Get Search Dictionary

1. Click on "Get Search Dictionary" query under your collection.
2. Press "**Send**" to send the request.
3. You will receive response at the bottom panel

### PHP sample

#### Add Track

`add-track.php`
Open the file, replace `$apiKey` `$audioPath` `$customer_filename`with your own API key and the local path that stores the audio file and filename. Replace remaining fields if necessary. This script uploads the audio files in the folder onto Musiio Tagging Service. To run:

```bash
php add-track.php
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

#### Update Track

`update-track.php`
Open the file, replace `$apiKey` `$track_id` with your own API key and the track ID . Replace remaining fields if necessary. This script uploads the audio files in the folder onto Musiio Tagging Service. To run:

```bash
php update-track.php
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

#### Get Track

`get-track.php`
Open the file, replace `$apiKey` `$track_id` with your own API key and the track ID. Replace remaining fields if necessary. This script uploads the audio files in the folder onto Musiio Tagging Service. To run:

```bash
php get-track.php
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

### Python sample

Python sample is stored under `samples/search/python`

#### Set up running environment

To install all the dependencies necessary for the scripts. Run the following code in your terminal:

For Mac

```bash
cd samples/search/python
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

For Windows

```bash
cd samples\search\python
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```

To deactivate virtual environment

```bash
deactivate
```

#### Add Track

`add-track.py`

You are required to input `api_key`,`audio_file`,`customer_filename`. The rest of the fields are optional

To run:

```bash
python add-track.py
```

#### Update Track

`update-track.py`

You are required to input `api_key`,`track_id`. The rest of the fields are optional

To run:

```bash
python update-track.py
```

####  Get Track

`get-track.py`

You are required to input `api_key`,`track_id`.

To run:

```bash
python get-track.py
```

#### Delete Track

`delete-track.py`

You are required to input `api_key`,`track_id`. 

To run:

```bash
python delete-track.py
```

#### Catalog Info

`catalog-info.py`

You are required to input `api_key`. 

To run:

```bash
python catalog-info.py
```

#### Upload File

`upload-file.py`

You are required to input `api_key`,`audio_file`. 

To run:

```bash
python upload-file.py
```

#### Upload YouTube Link

`upload-youtube-link.py`

You are required to input `api_key`,`youtube_link`. 

To run:

```bash
python upload-youtube-link.py
```

#### Extract Search Features

`extract-search-features.py`

You are required to input `api_key`,`track_id`. 

To run:

```bash
python extract-search-features.py
```

#### Perform Search

`perform-search.py`

You are required to input `api_key`,`track_id`, `search_text`. You can specify the page number in `page` and number of items per page in `items` 

To run:

```bash
python perform-search.py
```

#### Get Search Dictionary

`get-search-dictionary.py`

You are required to input `api_key`. 

To run:

```bash
python get-search-dictionary.py
```

#### 