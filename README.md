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
       "tags": ["CONTENT TYPE", "GENRE V3", "MOOD", "BPM", "KEY", "KEY SHARP", "ENERGY", "INSTRUMENTATION"]
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

### JavaScript (Frontend) sample

JavaScript ( frontend ) tagging sample is to be integrated with frontend web application. Constants required are to be passed in. You can find the code sample in `samples/tagging/js/` folder. Response will be logged in web client console.

#### Upload Audio File

`upload-audio-file.js`

Input required `API_KEY` 

Input file needs to be obtained from the `<input>` tag, as shown in the example below:

 ```html
<input type="file" id="fileInput">
...
<script>
    var fileInput = document.getElementById("fileInput");
</script>
 ```

#### Upload YouTube Link

`upload-youtube-link.js`

Input required `API_KEY`, `YOUTUBE_LINK`. 

#### Upload Audio Link

`upload-audio-link.js`

Input required `API_KEY`, `AUDIO_LINK`. 

#### Extract Tags

`extract-tags.js`

Input required `API_KEY`, `TRACK_ID`. 

Available tags: 

`["CONTENT TYPE", "GENRE V3", "MOOD", "BPM", "KEY", "KEY SHARP", "ENERGY", "INSTRUMENTATION"]`

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

### Java sample

`samples/tagging/java`

#### Set up Maven project

The Java sample shown here uses `Maven` as the Java project management tool. Hence, a `pom.xml` file is required for installing dependencies necessary to run the code samples. A detailed instruction on how to create a Maven project can be found here: https://spring.io/guides/gs/maven/

Initialize your Maven project, in this example, we will use the following project configuration:

```
<groupId>com.example.tagging</groupId>
<artifactId>tagging</artifactId>
```

Your project structure will look something like this:

```
(/samples/tagging/java/)
- tagging/
  | - src/
  |   | - main/com/example/tagging/
  |   | - test/
  | - target/
  | - pom.xml
```

Open `pom.xml` and add the following dependencies in the `<dependencies></dependencies>` tag

```xml
<!-- https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-web -->
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-web</artifactId>
  <version>2.3.3.RELEASE</version>
</dependency>
```

Copy and paste the code samples Java files in `samples/tagging/java/` into your project folder `tagging/src/main/com/example/tagging/` such that your project structure looks something like this:

```
(/samples/tagging/java/)
- tagging/
  | - src/
  |   | - main/com/example/tagging/
  |   |   | - AudioLinkUpload.java
  |   |   |	- AudioUpload.java
  |   |   |	- YoutubeUpload.java
  |   |   |	- ExtractTags.java
  |   |   | - HeadersUtils.java	(utility file)
  |   | - test/
  | - target/
  | - pom.xml
```

Once you are done, go back to the root directory of your project, in this case:

```bash
cd samples/tagging/java/tagging
```

and then follow the commands below to run each file.

#### Upload Audio File

`AudioUpload.java`

* Replcae package name with your own project group ID, (in our case here: `com.example.tagging`)

  ```java
  package com.example.tagging;
  ...
  ```

Required:  `API_KEY` 

To run: 

```bash
mvn exec:java -Dexec.mainClass="com.example.tagging.AudioUpload" -Dexec.args="audio file path here"
```

[Note: replace `com.example.tagging` with your own project group ID]

#### Upload Audio Link

`AudioLinkUpload.java`

* Replcae package name with your own project group ID, (in our case here: `com.example.tagging`)

  ```java
  package com.example.tagging;
  ...
  ```

Required: `API_KEY`

To run:

```bash
mvn exec:java -Dexec.mainClass="com.example.tagging.AudioLinkUpload" -Dexec.args="audio link here"
```

[Note: replace `com.example.tagging` with your own project group ID]

#### Upload YouTube Link

`YouTubeUpload.java`

* Replcae package name with your own project group ID, (in our case here: `com.example.tagging`)

  ```java
  package com.example.tagging;
  ...
  ```

Required:  `API_KEY`

To run:

```bash
mvn exec:java -Dexec.mainClass="com.example.tagging.YoutubeUpload" -Dexec.args="Youtube link here"
```

[Note: replace `com.example.tagging` with your own project group ID]

#### Extract Tags

`ExtractTags.java`

* Replcae package name with your own project group ID, (in our case here: `com.example.tagging`)

  ```java
  package com.example.tagging;
  ...
  ```

Required:  `API_KEY`

To run:

```bash
mvn exec:java -Dexec.mainClass="com.example.tagging.ExtractTags" -Dexec.args="track ID here"
```

[Note: replace `com.example.tagging` with your own project group ID]

### Node.js sample

#### Set up dependency

```bash
cd samples/tagging/node
npm install
```

#### Upload Audio File

`upload-audio-file.js\
Open the file, replace `API_KEY` `AUDIO_PATH` with your own API key and the local path that stores the audio file. This script uploads the audio files in the folder onto Musiio Tagging Service. To run:

```bash
node upload-audio-file.js
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

#### Upload YouTube Link

`upload-youtube-link.js`\
Open the file, replace `API_KEY` `YOUTUBE_LINK` with your own API key and the youtube track link. This script upload the youtube track onto Musiio Tagging Service. To run:

```bash
node upload-youtube-link.js
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

#### Upload Audio Link

`upload-audio-link.js`\
Open the file, replace `API_KEY` `AUDIO_LINK` with your own API key and the youtube track link. This script upload the youtube track onto Musiio Tagging Service. To run:

```bash
node upload-audio-link.js
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

#### Extract Tags

`extract-tags.js`
Open the file, replace `API_KEY` `TRACK_ID` with your own API key and the Track ID generated after the upload. This script will run the Tagging Service and return the tagging results in the console.

```bash
node extract-tags.js
```

The response will be printed out in the console.

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
2. Under "track" click on "Select Files" under VALUE to select your audio file. 
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

You are required to input `$apiKey`,`$audioPath`. The rest of the fields are optional

To run:

```bash
php add-track.php
```

#### Update Track

`update-track.php`

You are required to input `$apiKey`,`$track_id`. The rest of the fields are optional

To run:

```bash
php update-track.php
```

####  Get Track

`get-track.php`

You are required to input `$apiKey`,`$track_id`.

To run:

```bash
php get-track.php
```

#### Delete Track

`delete-track.php`

You are required to input `$apiKey`,`$track_id`. 

To run:

```bash
php delete-track.php
```

#### Catalog Info

`catalog-info.php`

You are required to input `$apiKey`. 

To run:

```bash
php catalog-info.php
```

#### Upload File

`upload-file.php`

You are required to input `$apiKey`,`$audioFilePath`. 

To run:

```bash
php upload-file.php
```

#### Upload YouTube Link

`upload-youtube-link.php`

You are required to input `$apiKey`,`$youtubeUrl`. 

To run:

```bash
php upload-youtube-link.php
```

#### Extract Search Features

`extract-search-features.php`

You are required to input `$apiKey`,`$trackID`. 

To run:

```bash
php extract-search-features.php
```

#### Perform Search

`perform-search.php`

You are required to input `$apiKey`,`$trackID`. You can specify the search text in `$searchText`, the page number in `page` and number of items per page in `items` 

To run:

```bash
php perform-search.php
```

#### Get Search Dictionary

`get-search-dictionary.php`

You are required to input `$apiKey`. 

To run:

```bash
php get-search-dictionary.php
```



### JavaScript (Frontend) sample

JavaScript ( frontend ) search sample is to be integrated with frontend web application. Constants required are to be passed in. You can find the code sample in `samples/search/js/` folder. Response will be logged in web client console.

#### Add Track

`add-track.js`

You are required to input `API_KEY`. 

Input audio file needs to be obtained from the `<input>` tag, as shown in the example below:

 ```html
<input type="file" id="fileInput">
...
<script>
    var fileInput = document.getElementById("fileInput");
</script>
 ```

The rest of the fields are optional

#### Update Track

`update-track.js`

You are required to input `API_KEY`,`TRACK_ID`. The rest of the fields are optional

####  Get Track

`get-track.js`

You are required to input `API_KEY`,`TRACK_ID`.

#### Delete Track

`delete-track.js`

You are required to input `API_KEY`,`TRACK_ID`. 

#### Catalog Info

`catalog-info.js`

You are required to input `API_KEY`. 

#### Upload File

`upload-file.js`

You are required to input `API_KEY` 

Input audio file needs to be obtained from the `<input>` tag, as shown in the example below:

 ```html
<input type="file" id="fileInput">
...
<script>
    var fileInput = document.getElementById("fileInput");
</script>
 ```

#### Upload YouTube Link

`upload-youtube-link.js`

You are required to input `API_KEY`,`YOUTUBE_LINK`. 

#### Extract Search Features

`extract-search-features.js`

You are required to input `API_KEY`,`TRACK_ID`. 

#### Perform Search

`perform-search.js`

You are required to input `API_KEY`,`TRACK_ID`. You can specify the search text in `SEARCH_TEXT`, page number in `page` and number of items per page in `items` 

#### Get Search Dictionary

`get-search-dictionary.js`

You are required to input `API_KEY`. 

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

You are required to input `api_key`,`audio_file`. The rest of the fields are optional

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

You are required to input `API_KEY`,`TRACK_ID`. You can specify the search text in `SEARCH_TEXT`, page number in `page` and number of items per page in `items` 

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
### Java sample

`samples/search/java`

#### Set up Maven project

The Java sample shown here uses `Maven` as the Java project management tool. Hence, a `pom.xml` file is required for installing dependencies necessary to run the code samples. A detailed instruction on how to create a Maven project can be found here: https://spring.io/guides/gs/maven/

Initialize your Maven project, in this example, we will use the following project configuration:

```
<groupId>com.example.search</groupId>
<artifactId>search</artifactId>
```

Your project structure will look something like this:

```
(/samples/search/java/)
- search/
  | - src/
  |   | - main/com/example/search/
  |   | - test/
  | - target/
  | - pom.xml
```

Open `pom.xml` and add the following dependencies in the `<dependencies></dependencies>` tag

```xml
<!-- https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-web -->
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-web</artifactId>
  <version>2.3.3.RELEASE</version>
</dependency>
```

Copy and paste the code samples Java files in `samples/search/java/` into your project folder `search/src/main/com/example/search/` such that your project structure looks something like this:

```
(/samples/search/java/)
- search/
  | - src/
  |   | - main/com/example/search/
  |   |   | - AddTrack.java
  |   |   | - UpdateTrack.java
  |   |   | - GetTrack.java
  |   |   | - DeleteTrack.java
  |   |   | - CatalogInfo.java
  |   |   | - AudioUpload.java
  |   |   | - YouTubeUpload.java
  |   |   | - ExtractSearchFeatures.java
  |   |   | - PerformSearch.java
  |   |   | - GetSearchDictionary.java
  |   |   | - HeadersUtils.java	(utility file)
  |   | - test/
  | - target/
  | - pom.xml
```

Once you are done, go back to the root directory of your project, in this case:

```bash
cd samples/search/java/search
```

and then follow the commands below to run each file.

#### Add Track

`AddTrack.java`

* Replcae package name with your own project group ID, (in our case here: `com.example.search`)

  ```java
  package com.example.search;
  ...
  ```

Required:  `API_KEY`

To run: 

```bash
mvn exec:java -Dexec.mainClass="com.example.search.AddTrack" -Dexec.args="audio file path here"
```

[Note: replace `com.example.search` with your own project group ID]

#### Update Track

`UpdateTrack.java`

* Replcae package name with your own project group ID, (in our case here: `com.example.search`)

  ```java
  package com.example.search;
  ...
  ```

Required:  `API_KEY`

To run: 

```bash
mvn exec:java -Dexec.mainClass="com.example.search.UpdateTrack" -Dexec.args="track ID here"
```

[Note: replace `com.example.search` with your own project group ID]

#### Get Track

`GetTrack.java`

* Replcae package name with your own project group ID, (in our case here: `com.example.search`)

  ```java
  package com.example.search;
  ...
  ```

Required: `API_KEY`

To run: 

```bash
mvn exec:java -Dexec.mainClass="com.example.search.GetTrack" -Dexec.args="track ID here"
```

[Note: replace `com.example.search` with your own project group ID]

#### Delete Track

`DeleteTrack.java`

* Replcae package name with your own project group ID, (in our case here: `com.example.search`)

  ```java
  package com.example.search;
  ...
  ```

Required:  `API_KEY`

To run: 

```bash
mvn exec:java -Dexec.mainClass="com.example.search.DeleteTrack" -Dexec.args="track ID here"
```

[Note: replace `com.example.search` with your own project group ID]

#### Catalog Info

`CatalogInfo.java`

* Replcae package name with your own project group ID, (in our case here: `com.example.search`)

  ```java
  package com.example.search;
  ...
  ```

Required: `API_KEY`

To run: 

```bash
mvn exec:java -Dexec.mainClass="com.example.search.CatalogInfo"
```

[Note: replace `com.example.search` with your own project group ID]

#### Upload Audio File

`AudioUpload.java`

* Replcae package name with your own project group ID, (in our case here: `com.example.search`)

  ```java
  package com.example.search;
  ...
  ```

Required: `API_KEY`

To run: 

```bash
mvn exec:java -Dexec.mainClass="com.example.search.AudioUpload" -Dexec.args="audio file path here"
```

[Note: replace `com.example.search` with your own project group ID]

#### Upload YouTube Link

`YoutubeUpload.java`

* Replcae package name with your own project group ID, (in our case here: `com.example.search`)

  ```java
  package com.example.search;
  ...
  ```

Required: `API_KEY`

To run: 

```bash
mvn exec:java -Dexec.mainClass="com.example.search.YoutubeUpload" -Dexec.args="youtube link here"
```

[Note: replace `com.example.search` with your own project group ID]

#### Extract Search Features

`ExtractSearchFeatures.java`

* Replcae package name with your own project group ID, (in our case here: `com.example.search`)

  ```java
  package com.example.search;
  ...
  ```

Required: `API_KEY`

To run: 

```bash
mvn exec:java -Dexec.mainClass="com.example.search.ExtractSearchFeatures" -Dexec.args="track ID here"
```

[Note: replace `com.example.search` with your own project group ID]

#### Perform Search

`PerformSearch.java`

* Replcae package name with your own project group ID, (in our case here: `com.example.search`)

  ```java
  package com.example.search;
  ...
  ```

Required: `API_KEY`

Optional: `searchText`, `page`, `items`

​		Specify the optional arguments in the command line followed by the track ID, only integer values are allowed for `page` and `items`. If unspecified, `searchText` is deafult empty, `page` default to be 0, `items` default to be 50.

To run: 

```bash
mvn exec:java -Dexec.mainClass="com.example.search.PerformSearch" -Dexec.args="{track ID here} {searchText} {page} {items}"
```

Example:

```bash
mvn exec:java -Dexec.mainClass="com.example.search.PerformSearch" -Dexec.args="TMP_-biOGdYiF-I 'this is my search text' 1 20"
```

Meaning: use search text: 'this is my search text', query page number 1 and 20 items per page.

[Note: replace `com.example.search` with your own project group ID]

#### Get Search Dictionary

`GetSearchDictionary.java`

* Replcae package name with your own project group ID, (in our case here: `com.example.search`)

  ```java
  package com.example.search;
  ...
  ```

Required: `API_KEY`

To run: 

```bash
mvn exec:java -Dexec.mainClass="com.example.search.GetSearchDictionary"
```

[Note: replace `com.example.search` with your own project group ID]

### Node.js sample

Node sample is stored under `samples/search/node`

#### Set up running environment

To install all the dependencies necessary for the scripts. Run the following code in your terminal:

```bash
cd samples/search/node
npm install
```

#### Add Track

`add-track.js`

You are required to input `API_KEY`,`AUDIO_PATH`. The rest of the fields are optional

To run:

```bash
node add-track.js
```

#### Update Track

`update-track.js`

You are required to input `API_KEY`,`TRACK_ID`. The rest of the fields are optional

To run:

```bash
node update-track.js
```

####  Get Track

`get-track.js`

You are required to input `API_KEY`,`TRACK_ID`.

To run:

```bash
node get-track.js
```

#### Delete Track

`delete-track.js`

You are required to input `API_KEY`,`TRACK_ID`. 

To run:

```bash
node delete-track.js
```

#### Catalog Info

`catalog-info.js`

You are required to input `API_KEY`. 

To run:

```bash
node catalog-info.js
```

#### Upload File

`upload-file.js`

You are required to input `API_KEY`,`AUDIO_PATH`. 

To run:

```bash
node upload-file.js
```

#### Upload YouTube Link

`upload-youtube-link.js`

You are required to input `API_KEY`,`YOUTUBE_LINK`. 

To run:

```bash
node upload-youtube-link.js
```

#### Extract Search Features

`extract-search-features.js`

You are required to input `API_KEY`,`TRACK_ID`. 

To run:

```bash
node extract-search-features.js
```

#### Perform Search

`perform-search.js`

You are required to input `API_KEY`,`TRACK_ID`You can specify search text in `SEARCH_TEXT`, the page number in `PAGE` and number of items per page in `ITEMS_PER_PAGE` 

To run:

```bash
node perform-search.js
```

#### Get Search Dictionary

`get-search-dictionary.js`

You are required to input `API_KEY`. 

To run:

```bash
node get-search-dictionary.js
```
