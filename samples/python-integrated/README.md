# Python Integrated Samples

Contains scripts that take multiple audio tracks in one folder and tag them one-by-one and output into CSV file.

**Python version:** 3.6.8

[generate_tags.py](generate_tags.py):
tag audio tracks located in a given folder and save tags in .json format for each track\

[tags_to_csv.py](tags_to_csv.py):
check all tag .json files located in a given folder and write the tags to a single CSV file\

[constants.py](constants.py):
update the values of 'KEY' and 'BASE_URL' with your Musiio API Key and API Url\

## Installation

```bash
cd samples\tagging\python-integrated
virtualenv venv
venv\Scripts\activate
pip install -r requirements
```

## Update constants.py with API Key

```python
KEY = "Replace With Your Musiio API KEY"
BASE_URL = "Replace with Your API URL"
```

## Tag Generation

```bash
python generate_tags.py --source-path <source path> --destination-path <destination path> --tag-selection "content type" "genre" "bpm" "key" "mood" "energy" "instrumentation"
```

## Convert Tags to CSV

```bash
python tags_to_csv.py --tags-path <tags path> --tags-csv <destination path for csv> --tags-types "genre" "genre secondary" "mood" "mood secondary" "energy" "vocal presence" "instrument"
```
