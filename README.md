# tagging-sample
Sample code for how to use the Musiio API
generate_tags.py: tag audio tracks located in a given folder and save tags in .json format for each track
tags_to_csv.py: check all tag .json files located in a given folder and write the tags to a single CSV file

## Update constants.py with API Key
```python
KEY = "Replace With Your API KEY"
```

## Tag Generation

```bash
cd musiio_tagging_scripts
python generate_tags.py --source-path C:/tagging_scripts/tracks --destination-path C:/tagging_scripts/tags --tag-selection "content type" "genre" "bpm" "key" "mood" "energy" "instrumentation"
```

## Convert Tags to CSV
```bash
cd musiio_tagging_scripts
python tags_to_csv.py --tags-path C:/tagging_scripts/tags --tags-csv C:/tagging_scripts --tags-types "genre" "genre secondary" "mood" "mood secondary" "energy" "vocal presence" "instrument"
```


# GUI Usage

## Tag Generation
![Tag Generation](https://raw.githubusercontent.com/username/projectname/branch/path/to/img.png)
```text
Source Folder: The folder where your audio tracks are stored
Destination Folder: The folder where you want your tag jsons to be saved
API Key: Replace with your Musiio API Key
```

## Convert Tags to CSV
![Convert Tags to CSV](https://raw.githubusercontent.com/username/projectname/branch/path/to/img.png)
```text
Tag Folder: The folder containing your tag jsons 
Write CSV to Directory: The folder where the CSV will be saved
```
