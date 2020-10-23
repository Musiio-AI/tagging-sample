# Python Individual Samples

Contains scripts that handle individual track tagging.

## Set up running environment

To install all the dependencies necessary for the scripts. Run the following code in your terminal:

For Mac:

```bash
cd samples/tagging/python-individual
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

For Windows:

```bash
cd samples\tagging\python-individual
virtualenv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

To deactivate virtual environment

```bash
deactivate
```
## Upload Audio File

[upload-audio-file.py](upload-audio-file.py)

Input required `api_key`, `audio_file`.

To run:

```bash
python upload-audio-file.py
```

## Upload YouTube Link

[upload-youtube-link.py](upload-youtube-link.py)

Input required `api_key`, `youtube_link`.

To run:

```bash
python upload-youtube-link.py
```

## Upload Audio Link

[upload-audio-link.py](upload-audio-link.py)

Input required `api_key`, `audio_link`.

To run:

```bash
python upload-audio-link.py
```

## Extract Tags

[extract-tags.py](extract-tags.py)

Input required `api_key`, `track-id`.

Available tags:

`["CONTENT TYPE", "GENRE V3", "MOOD", "BPM", "KEY", "KEY SHARP", "ENERGY", "INSTRUMENTATION"]`

To run:

```bash
python extract-tags.py
```
