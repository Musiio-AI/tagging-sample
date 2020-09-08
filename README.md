# Musiio Tagging Code Sample

This repository contains code samples for using Musiio API **Tagging** service. Tagging is that given input tracks via audio files or YouTube links, the Tagging service will return a list of classifications that the Musiio AI predicts for a particular track, for example, content type, bpm, key, genre, instruments, etc. 

The code samples are put in `/samples`. Within each folder, you can find detailed code samples for various languages such as Python, PHP, Java, JavaScript and Node.js. A Postman collection is also provided in the documentation below for users who would like to try out in the GUI first.

Below is a breakdown of the code sample repository structure:

```
Musiio Tagging Code Sample (./samples/)
|
|--python-individual/	(to run with single track)
|--python-integrated/	(to run with bulk upload)
|--java/	(Java samples)
|--php/		(PHP samples)
|--js/	(JavaScript samples)
|--node/	(Node.js samples)
```

## Table of Contents

[Postman Collection](#postman-collection)

* [How to set up postman samples](#how-to-set-up-postman-samples)
* [Upload Audio File](#upload-audio-file)
* [Upload YouTube Link](#upload-youtube-link)
* [Upload Audio Link](#upload-audio-link)
* [Extract Tags](#extract-tags)

[PHP Sample](#php-sample)

* [Upload Audio File](#upload-audio-file-1)
* [Upload YouTube Link](#upload-youtube-link-1)
* [Upload Audio Link](#upload-audio-link-1)
* [Extract Tags](#extract-tags-1)

[JavaScript Sample](#javascript-sample)

* [Upload Audio File](#upload-audio-file-2)
* [Upload YouTube Link](#upload-youtube-link-2)
* [Upload Audio Link](#upload-audio-link-2)
* [Extract Tags](#extract-tags-2)

[Python Individual Sample](#python-indiviual-sample)

* [Set up running environment](#set-up-running-environment)
* [Upload Audio File](#upload-audio-file-3)
* [Upload YouTube Link](#upload-youtube-link-3)
* [Upload Audio Link](#upload-audio-link-3)
* [Extract Tags](#extract-tags-3)

[Python Integrated Sample](#python-integrated-sample)

* [Installation](#installation)
* [Update constants.py with API Key](#update-constantspy-with-api-key)
* [Tag Generation](#tag-generation)
* [Convert Tags to CSV](#convert-tags-to-csv)

[Java Sample](#java-sample)

* [Set up Maven project](#set-up-maven-project)
* [Upload Audio File](#upload-audio-file-4)
* [Upload Audio Link](#upload-audio-link-4)
* [Upload YouTube Link](#upload-youtube-link-4)
* [Extract Tags](#extract-tags-4)

[Node.js Sample](#nodejs-sample)

* [Set up dependency](#set-up-dependency)
* [Upload Audio File](#upload-audio-file-5)
* [Upload YouTube Link](#upload-youtube-link-5)
* [Upload Audio Link](#upload-audio-link-5)
* [Extract Tags](#extract-tags-5)

[Windows Executable GUI](#windows-executable-gui)

* [Tag Generation](#tag-generation-1)
* [Convert Tags to CSV](#convert-tags-to-csv-1)

[Rebuilding the GUI](#rebuilding-the-gui)

* [Windows](#windows)
* [Mac](#mac)

## Postman Collection

If you don't have postman, download here: https://www.postman.com/downloads/

Here is the collection public link:

https://www.getpostman.com/collections/2d47eb75d66a50ed4308

### How to set up postman samples

1. Download postman and install it.
2. Open postman, at the top left corner click on "Import" button
3. Choose "Link" tab
4. Copy paste the collection public link in and click "Continue"
5. Press "Import" to import the collection
6. You will see the collection folder appears on the left-side panel. Click to expand to see individual request query.
7. Now you need to add your API key in to authorize your request. Click on the "three dots" icon on the right of the collection folder tab when your mouse hovers on it. Click "Edit". Under the "Authorization" tab, select "Basic Auth" and copy paste your **Tagging API key** into the "username" field. Leave the "password" field empty. Click "Update" to update your collection.

Now you are all set and it is time to use the sample.

### Upload Audio File

1. Click on "Upload Audio File" query under your collection. On the main panel, click on "Body" and select "form-data"
2. Input KEY as "audio" and press "Select Files" under VALUE to select an audio file to be uploaded
3. Press "**Send**" to send the request.

You will receive response at the bottom panel

### Upload YouTube Link

1. Click on "Upload YouTube Link" query under your collection. On the main panel, click on "Body" and select "raw", on the right select "JSON" in the dropdown menu.
2. Input the following into the textbox:

   ```json
   {
   	"link": "YOUR YOUTUBE LINK HERE"
   }
   ```

3. Press "**Send**" to send the request.

You will receive response at the bottom panel

### Upload Audio Link

1. Click on "Upload Audio Link" query under your collection. On the main panel, click on "Body" and select "raw", on the right select "JSON" in the dropdown menu.
2. Input the following into the textbox:

   ```json
   {
   	"link": "YOUR AUDIO LINK HERE"
   }
   ```
3. Press "**Send**" to send the request.
4. You will receive response at the bottom panel
### Extract Tags

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

## PHP sample
### Upload Audio File

`audio-upload.php`\
Open the file, replace `$apiKey` `$audioPath` with your own API key and the local path that stores the audio file. This script uploads the audio files in the folder onto Musiio Tagging Service. To run:

```bash
php audio-upload.php
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

### Upload YouTube Link

`youtube-upload.php`\
Open the file, replace `$apiKey` `$youtubeUrl` with your own API key and the youtube track link. This script upload the youtube track onto Musiio Tagging Service. To run:

```bash
php youtube-upload.php
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

### Upload Audio Link

`upload-audio-link.php`\
Open the file, replace `$apiKey` `$audioLink` with your own API key and the youtube track link. This script upload the youtube track onto Musiio Tagging Service. To run:

```bash
php upload-audio-link.php
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

### Extract Tags

`extract-tags.php`\
Open the file, replace `$apiKey` `$trackId` with your own API key and the Track ID generated after the upload. This script will run the Tagging Service and return the tagging results in the console.

```bash
php extract-tags.php
```

The response will be printed out in the console.

## JavaScript (Frontend) sample

JavaScript ( frontend ) tagging sample is to be integrated with frontend web application. Constants required are to be passed in. You can find the code sample in `samples/js/` folder. Response will be logged in web client console.

### Upload Audio File

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
### Upload YouTube Link

`upload-youtube-link.js`

Input required `API_KEY`, `YOUTUBE_LINK`. 

### Upload Audio Link

`upload-audio-link.js`

Input required `API_KEY`, `AUDIO_LINK`. 

### Extract Tags

`extract-tags.js`

Input required `API_KEY`, `TRACK_ID`. 

Available tags: 

`["CONTENT TYPE", "GENRE V3", "MOOD", "BPM", "KEY", "KEY SHARP", "ENERGY", "INSTRUMENTATION"]`

## Python individual sample

The folder `samples/python-individual` contains scripts that handle individual track tagging

### Set up running environment

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
### Upload Audio File

`upload-audio-file.py`

Input required `api_key`, `audio_file`. 

To run:

```bash
python upload-audio-file.py
```

### Upload YouTube Link

`upload-youtube-link.py`

Input required `api_key`, `youtube_link`. 

To run:

```bash
python upload-youtube-link.py
```

### Upload Audio Link

`upload-audio-link.py`

Input required `api_key`, `audio_link`. 

To run:

```bash
python upload-audio-link.py
```

### Extract Tags

`extract-tags.py`

Input required `api_key`, `track-id`. 

Available tags: 

`["CONTENT TYPE", "GENRE V3", "MOOD", "BPM", "KEY", "KEY SHARP", "ENERGY", "INSTRUMENTATION"]`

To run:

```bash
python extract-tags.py
```

## Python Integrated sample

The folder `samples/python-integrated` contains scripts that take multiple audio tracks in one folder and tag them one-by-one and output into CSV file.

**Python version:** 3.6.8
`generate_tags.py`
tag audio tracks located in a given folder and save tags in .json format for each track\
`tags_to_csv.py`
check all tag .json files located in a given folder and write the tags to a single CSV file\
`constants.py`
update the values of 'KEY' and 'BASE_URL' with your Musiio API Key and API Url\

### Installation

```bash
cd samples\tagging\python-integrated
virtualenv venv
venv\Scripts\activate
pip install -r requirements
```

### Update constants.py with API Key

```python
KEY = "Replace With Your Musiio API KEY"
BASE_URL = "Replace with Your API URL"
```

### Tag Generation

```bash
python generate_tags.py --source-path C:/tagging_scripts/tracks --destination-path C:/tagging_scripts/tags --tag-selection "content type" "genre" "bpm" "key" "mood" "energy" "instrumentation"
```

### Convert Tags to CSV

```bash
python tags_to_csv.py --tags-path C:/tagging_scripts/tags --tags-csv C:/tagging_scripts --tags-types "genre" "genre secondary" "mood" "mood secondary" "energy" "vocal presence" "instrument"
```

## Java sample

`samples/java`

### Set up Maven project

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

### Upload Audio File

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

### Upload Audio Link

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

### Upload YouTube Link

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

### Extract Tags

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

## Node.js sample

### Set up dependency

```bash
cd samples/tagging/node
npm install
```

### Upload Audio File

`upload-audio-file.js\
Open the file, replace `API_KEY` `AUDIO_PATH` with your own API key and the local path that stores the audio file. This script uploads the audio files in the folder onto Musiio Tagging Service. To run:

```bash
node upload-audio-file.js
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

### Upload YouTube Link

`upload-youtube-link.js`\
Open the file, replace `API_KEY` `YOUTUBE_LINK` with your own API key and the youtube track link. This script upload the youtube track onto Musiio Tagging Service. To run:

```bash
node upload-youtube-link.js
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

### Upload Audio Link

`upload-audio-link.js`\
Open the file, replace `API_KEY` `AUDIO_LINK` with your own API key and the youtube track link. This script upload the youtube track onto Musiio Tagging Service. To run:

```bash
node upload-audio-link.js
```

The response will be printed out in the console. The `id` field will be the Track ID for tagging extraction.

### Extract Tags

`extract-tags.js`
Open the file, replace `API_KEY` `TRACK_ID` with your own API key and the Track ID generated after the upload. This script will run the Tagging Service and return the tagging results in the console.

```bash
node extract-tags.js
```

The response will be printed out in the console.

## Windows Executable GUI Usage

Executables are located in the `windows` folder\
**Note:** GUI applications for MacOS are currently not available for distribution, but you should be able to build them yourself using the instructions below under 'Rebuilding the GUI'

### Tag Generation

**Source Folder:** The folder where your audio tracks are stored\
**Destination Folder:** The folder where you want your tag jsons to be saved\
**API Key:** Replace with your Musiio API Key

### Convert Tags to CSV

**Tag Folder:** The folder containing your tag jsons\
**Write CSV to Directory:** The folder where the CSV will be saved

## Rebuilding the GUI

### Windows
```bash
pip install pyinstaller
pyinstaller --onefile generate_tags_gui.py
```

### Mac
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
