# Windows Executable GUI Usage

Executables are located in the [*windows* folder](.)

**Note:** GUI applications for MacOS are currently not available for distribution, but you should be able to build them yourself using the instructions below under 'Rebuilding the GUI'

## Tag Generation

**Source Folder:** The folder where your audio tracks are stored\
**Destination Folder:** The folder where you want your tag json files to be saved\
**API Key:** Replace with your Musiio Tagging API Key

## Convert Tags to CSV

**Tag Folder:** The folder containing your tag json files\
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
